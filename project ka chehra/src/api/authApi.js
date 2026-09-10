import client from './client';

export const loginRequest = async (email, password) => {
  const res = await client.post('/auth/login', { email, password });
  return res.data; // { message, token, email, role }
};

export const registerRequest = async (userPayload, profileImageFile) => {
  const formData = new FormData();

  // Must be sent as application/json, or Spring's @RequestPart("user")
  // won't be able to deserialize it into a User object
  formData.append(
    'user',
    new Blob([JSON.stringify(userPayload)], { type: 'application/json' })
  );
  formData.append('profileImage', profileImageFile);

  const res = await client.post('/auth/register', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return res.data;
};