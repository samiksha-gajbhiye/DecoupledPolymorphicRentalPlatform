package com.sg.main.services;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.List;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.sg.main.entities.OrderItem;
import com.sg.main.entities.Product;
import com.sg.main.entities.RentalOrder;
import com.sg.main.entities.User;
import com.sg.main.entities.enums.RentalOrderStatus;
import com.sg.main.repositories.OrderItemRepository;
import com.sg.main.repositories.RentalOrderRepository;

@Service
public class RentalOrderService {

    @Autowired
    private RentalOrderRepository rentalOrderRepo;

    @Autowired
    private OrderItemRepository orderItemRepo;

    @Autowired
    private ProductService productService;

    /**
      Renter req karega product ki rent lene ke liye for a particular period
      and creates karega RentalOrder jiska status PENDING rahega
     */
    public RentalOrder requestRental(User customer, int productId, LocalDate startDate, LocalDate endDate, int quantity) {

        if (startDate == null || endDate == null || startDate.isAfter(endDate)) {
            throw new RuntimeException("Invalid date range: start date must be before end date");
        }

        if (startDate.isBefore(LocalDate.now())) {
            throw new RuntimeException("Cannot book a start date in the past");
        }

        if (quantity < 1) {
            throw new RuntimeException("Quantity must be at least 1");
        }

        Product product = productService.getProductById(productId);

        if (product.getUser() != null && product.getUser().getId() == customer.getId()) {
            throw new RuntimeException("You cannot rent your own product");
        }

        List<OrderItem> conflicts = orderItemRepo.findOverlappingOrderItems(productId, startDate, endDate);
        if (!conflicts.isEmpty()) {
            throw new RuntimeException("Product is already booked for the selected dates");
        }

        long durationDays = ChronoUnit.DAYS.between(startDate, endDate);
        if (durationDays < 1) {
            durationDays = 1; // minimum 1 din ka charge karega if same day ke liye order kiya ho
        }

        BigDecimal pricePerDay = product.getPricePerDay() != null ? product.getPricePerDay() : BigDecimal.ZERO;
        BigDecimal subTotal = pricePerDay.multiply(BigDecimal.valueOf(durationDays)).multiply(BigDecimal.valueOf(quantity));
        BigDecimal deposit = product.getSecurityDeposit() != null ? product.getSecurityDeposit() : BigDecimal.ZERO;
        BigDecimal discount = BigDecimal.ZERO; // no discount logic baad me change kar sakte hai
        BigDecimal grandTotal = subTotal.add(deposit).subtract(discount);

        RentalOrder order = new RentalOrder();
        order.setCustomer(customer);
        order.setOrderCode(UUID.randomUUID());
        order.setRentalStart(startDate);
        order.setRentalEnd(endDate);
        order.setQuantity(quantity);
        order.setSubTotal(subTotal);
        order.setDiscount(discount);
        order.setDeposit(deposit);
        order.setGrandTotal(grandTotal);
        order.setLateFee(BigDecimal.ZERO);
        order.setStatus(RentalOrderStatus.PENDING);
        // paymentStatus ko abhi ke  unset chhoda hai   payment flow is a separate from this section

        order = rentalOrderRepo.save(order);

        OrderItem item = new OrderItem();
        item.setOrder(order);
        item.setProduct(product);
        item.setPricePerDay(pricePerDay);
        item.setQuantity(quantity);
        item.setSubTotal(subTotal);
        item.setRentalDuration(durationDays);
        orderItemRepo.save(item);

        return order;
    }

    // Product owner pending req accept karega
    public RentalOrder confirmOrder(int orderId, User owner) {
        RentalOrder order = getOwnedOrderOrThrow(orderId, owner);

        if (order.getStatus() != RentalOrderStatus.PENDING) {
            throw new RuntimeException("Only pending orders can be confirmed");
        }

        // Recheck karega ki kisi ki same product kisi booked duration se conflict to nahi karega
        // mean time confirmed karega
        List<OrderItem> items = orderItemRepo.findByOrder_OrderId(orderId);
        for (OrderItem item : items) {
            List<OrderItem> conflicts = orderItemRepo.findOverlappingOrderItems(
                    item.getProduct().getProductId(), order.getRentalStart(), order.getRentalEnd());
            conflicts.removeIf(c -> c.getOrder().getOrderId() == orderId);

            boolean alreadyConfirmed = conflicts.stream()
                    .anyMatch(c -> c.getOrder().getStatus() == RentalOrderStatus.CONFIRMED
                            || c.getOrder().getStatus() == RentalOrderStatus.ACTIVE);
            if (alreadyConfirmed) {
                throw new RuntimeException("Another order for these dates was already confirmed");
            }
        }

        order.setStatus(RentalOrderStatus.CONFIRMED);
        return rentalOrderRepo.save(order);
    }

    // Owner ne  reject kiya ya  customer ne  cancel kiya check karega (pending/confirmed order)
    public RentalOrder cancelOrder(int orderId, User user, String reason) {
        RentalOrder order = rentalOrderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found: " + orderId));

        boolean isCustomer = order.getCustomer().getId() == user.getId();
        boolean isOwner = isOwnerOfOrder(order, user);

        if (!isCustomer && !isOwner) {
            throw new RuntimeException("You are not authorized to cancel this order");
        }

        if (order.getStatus() == RentalOrderStatus.COMPLETED || order.getStatus() == RentalOrderStatus.CANCELLED) {
            throw new RuntimeException("This order cannot be cancelled");
        }

        order.setStatus(RentalOrderStatus.CANCELLED);
        order.setCancellationReason(reason);
        order.setCancelledAt(LocalDateTime.now());
        return rentalOrderRepo.save(order);
    }

    public List<RentalOrder> getMyOrders(User customer) {
        return rentalOrderRepo.findByCustomer_Id(customer.getId());
    }

    public List<RentalOrder> getIncomingOrders(User owner) {
        List<OrderItem> items = orderItemRepo.findByProduct_User_Id(owner.getId());
        return items.stream()
                .map(OrderItem::getOrder)
                .distinct()
                .toList();
    }

    private RentalOrder getOwnedOrderOrThrow(int orderId, User owner) {
        RentalOrder order = rentalOrderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found: " + orderId));

        if (!isOwnerOfOrder(order, owner)) {
            throw new RuntimeException("You do not own the product(s) in this order");
        }

        return order;
    }

    private boolean isOwnerOfOrder(RentalOrder order, User owner) {
        List<OrderItem> items = orderItemRepo.findByOrder_OrderId(order.getOrderId());
        return items.stream()
                .anyMatch(item -> item.getProduct().getUser() != null
                        && item.getProduct().getUser().getId() == owner.getId());
    }
}