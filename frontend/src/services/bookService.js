import axios from 'axios';

const API_URL = '/api/books/';

export const getBooks = () => axios.get(API_URL);
export const getBook = (id) => axios.get(`${API_URL}${id}/`);
export const createBook = (data, token) =>
  axios.post(API_URL, data, {
    headers: { Authorization: `Bearer ${token}` },
  });
export const updateBook = (id, data, token) =>
  axios.put(`${API_URL}${id}/`, data, {
    headers: { Authorization: `Bearer ${token}` },
  });
export const deleteBook = (id, token) =>
  axios.delete(`${API_URL}${id}/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
export const searchBooks = (query) => axios.get(`${API_URL}?search=${query}`);
export const getBooksByAuthor = (authorId) =>axios.get(`${API_URL}?author=${authorId}`);   
