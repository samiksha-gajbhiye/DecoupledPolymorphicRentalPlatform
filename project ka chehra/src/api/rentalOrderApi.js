import client from './client';

export const createRentalOrder = async ({ customerCode, startDate, endDate, items }) => {
  const res = await client.post('/rentalOrder/orderRequest', {
    customerCode, startDate, endDate, items,
  });
  return res.data;
};

export const cancelRentalOrder = async (orderCode, customerCode) => {
  const res = await client.post('/rentalOrder/cancelOrder', { orderCode, customerCode });
  return res.data;
};

export const confirmRentalOrder = async (orderCode, ownerCode) => {
  const res = await client.post('/rentalOrder/confirmOrder', { orderCode, ownerCode });
  return res.data;
};