import { API_PATH_BOOKS, BASE_HTTP_URL } from "./constants";
import { httpDelete, httpGet, httpPost, httpPut } from "./helper-functions";
import { Book } from "./types";

const BASE_CAR_URL = BASE_HTTP_URL + API_PATH_BOOKS;

export const getAvailableBooks = () => httpGet<Book[]>(`${BASE_CAR_URL}/available`);

export const getAllBooks = () => httpGet<Book[]>(`${BASE_CAR_URL}`);

export const getRelatedBooks = () => httpGet<Book[]>(`${BASE_CAR_URL}/related`);

export const addBook = (book: Book) => httpPost(BASE_CAR_URL, book);

export const updateBook = (book: Book) => httpPut(BASE_CAR_URL, book);

export const deleteBook = (bookId: number) => httpDelete(`${BASE_CAR_URL}/${bookId}`);
