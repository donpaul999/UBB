import { API_PATH_BOOKS, BASE_HTTP_URL } from "./constants";
import { httpDelete, httpGet, httpPost, httpPut } from "./helper-functions";
import {Book, IdMap, Change} from "./types";

const BASE_BOOK_URL = BASE_HTTP_URL + API_PATH_BOOKS;

export const getAllBooks = () => httpGet<Book[]>(`${BASE_BOOK_URL}`);

export const getRelatedBooks = (search: string, isBooked: boolean | null, start: number, count: number) => {
    const bookedQuery = isBooked === null ? "" : `&isBooked=${isBooked}`;

    return httpGet<Book[]>(`${BASE_BOOK_URL}/related?` +
        `searchKeyword=${search}${bookedQuery}&from=${start}&count=${count}`);
}

export const addBook = (book: Book) => httpPost(BASE_BOOK_URL, book);

export const updateBook = (book: Book) => httpPut(BASE_BOOK_URL, book);

export const deleteBook = (bookId: number) => httpDelete(`${BASE_BOOK_URL}/${bookId}`);

export const syncChanges = (changes: Change[]) =>
    httpPost<IdMap[]>(`${BASE_BOOK_URL}/sync`, changes);

const OnlineBookAccessor = {
    getRelatedBooks,
    addBook,
    updateBook,
    deleteBook,
    syncChanges
}

export default OnlineBookAccessor;
