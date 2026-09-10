import client, { BASE_URL } from './client';

export const getAllProducts = async () => {
  const res = await client.get('/product/all');
  return res.data;
};

export const getProductsByTitle = async (title) => {
  const res = await client.get(`/product/title/${encodeURIComponent(title)}`);
  return res.data;
};

export const getProductsByCategory = async (category) => {
  const res = await client.get(`/product/category/${encodeURIComponent(category)}`);
  return res.data;
};

export const addProduct = async (productPayload, imageFiles) => {
  const formData = new FormData();
  formData.append(
    'product',
    new Blob([JSON.stringify(productPayload)], { type: 'application/json' })
  );
  imageFiles.forEach((file) => formData.append('images', file));

  const res = await client.post('/product/add', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return res.data;
};

// Backend returns bare filenames for images; this turns them into real URLs
export const resolveImageUrl = (imageUrl) => {
  if (!imageUrl) return null;
  if (imageUrl.startsWith('http')) return imageUrl;
  return `${BASE_URL}${imageUrl}`;
};