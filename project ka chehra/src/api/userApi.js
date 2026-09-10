import client from './client';

export const getCurrentUser = async () => {
  const res = await client.get('/user/getUser');
  return res.data;
};

export const updateUser = async (userCode, userPayload) => {
  const res = await client.put(`/user/update/${userCode}`, userPayload);
  return res.data;
};

export const deleteUser = async (userCode) => {
  const res = await client.delete(`/user/delete/${userCode}`);
  return res.data;
};