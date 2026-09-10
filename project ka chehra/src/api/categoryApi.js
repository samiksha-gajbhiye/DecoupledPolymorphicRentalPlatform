import client from './client';

export const getAllCategories = async () => {
  const res = await client.get('/category/all');
  return res.data;
};