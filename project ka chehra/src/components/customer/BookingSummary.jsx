import { Calendar, CreditCard, ShieldCheck } from 'lucide-react';

const BookingSummary = ({ booking }) => {
  return (
    <div className="py-4">
      <div className="space-y-4">
        <div className="border-t border-gray-200 dark:border-gray-700 pt-4">
          <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-3">
            Booking Summary
          </h3>
          <div className="space-y-3">
            <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400">
              <span>Item:</span>
              <span>{booking.item.name}</span>
            </div>
            <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400">
              <span>Rental Period:</span>
              <span>{booking.dates.totalDays} days</span>
            </div>
            <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400">
              <span>Daily Rate:</span>
              <span>${booking.pricing.dailyRate}</span>
            </div>
            <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400">
              <span>Subtotal:</span>
              <span>${booking.pricing.subtotal}</span>
            </div>
            <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400">
              <span>Taxes:</span>
              <span>${booking.pricing.taxes}</span>
            </div>
            <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400">
              <span>Fees:</span>
              <span>${booking.pricing.fees}</span>
            </div>
            <div className="flex justify-between pt-2 border-t border-gray-200 dark:border-gray-700 text-lg font-medium">
              <span>Total:</span>
              <span>${booking.pricing.total}</span>
            </div>
          </div>
        </div>

        <div className="border-t border-gray-200 dark:border-gray-700 pt-4">
          <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-3">
            Payment Status
          </h3>
          <div className="flex items-center space-x-3">
            <div className="flex items-center justify-center w-8 h-8 bg-green-100 text-green-500 dark:bg-green-900 dark:text-green-400 rounded-full">
              <ShieldCheck className="h-4 w-4" />
            </div>
            <div>
              <p className="font-medium text-gray-900 dark:text-white">Payment Completed</p>
              <p className="text-sm text-gray-500 dark:text-gray-400">
                Payment of ${booking.pricing.total} was processed successfully
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BookingSummary;