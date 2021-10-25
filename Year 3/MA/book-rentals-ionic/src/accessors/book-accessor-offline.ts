import { RelatedBooksStorage } from "../infrastructure";
import { Book, IdMap } from "./types";

const FIRST_TEMPORARY_ID = -1;

export const getRelatedBooks = () => RelatedBooksStorage.get();

export const setRelatedBooks = async (books: Book[]) => {
    const existingBooks = await RelatedBooksStorage.get();

    await RelatedBooksStorage.set(merge(existingBooks, books));
}

export const addBook = async (book: Book) => {
    const books = await RelatedBooksStorage.get();

    if (!book.id) {
        book.id = getTemporaryId(books);
    }
    books.push(book);

    await RelatedBooksStorage.set(books);
}

export const updateBook = async (book: Book) => {
    const books = await RelatedBooksStorage.get();

    const indexOfModifiedBook = getIndexOfBook(books, book.id);
    books[indexOfModifiedBook] = book;

    await RelatedBooksStorage.set(books);
}

export const deleteBook = async (bookId: number) => {
    const books = await RelatedBooksStorage.get();

    const indexOfModifiedBook = getIndexOfBook(books, bookId);
    books.splice(indexOfModifiedBook, 1);

    await RelatedBooksStorage.set(books);
}

export const updateIds = async (idMapping: IdMap[]) => {
    const books = await RelatedBooksStorage.get();

    idMapping.forEach(({ from, to }) => {
        let bookIndexToUpdate = books.findIndex(({ id }) => from === id);
        while (bookIndexToUpdate > -1) {
            books[bookIndexToUpdate].id = to;
            bookIndexToUpdate = books.findIndex(({ id }) => from === id);
        }
    });

    await RelatedBooksStorage.set(books);
}

const getTemporaryId = (booksAsReference: Book[]) => {
    const bookIds = booksAsReference.map(book => book.id);
    const lastId = Math.min(...bookIds);

    return lastId > FIRST_TEMPORARY_ID ? FIRST_TEMPORARY_ID : lastId - 1;
}

const getIndexOfBook = (fromBooks: Book[], bookId: number) =>
    fromBooks.findIndex(book => book.id === bookId);

const merge = (localBooks: Book[], fetchedBooks: Book[]) => {
    fetchedBooks.forEach(book => {
        const existentBookIndex = localBooks.findIndex(({ id }) => id === book.id);

        if (existentBookIndex > -1) {
            localBooks[existentBookIndex] = book;
        } else {
            localBooks.push(book);
        }
    });

    return localBooks;
}

const OfflineBookAccessor = {
    getRelatedBooks,
    setRelatedBooks,
    addBook,
    updateBook,
    deleteBook,
    updateIds
}

export default OfflineBookAccessor;
