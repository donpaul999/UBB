import { LocalStorage } from "..";
import { Book } from "../../accessors/types";

export const BooksStorage = (key: string) => ({
    set: (books: Book[]) => LocalStorage.set<Book[]>(key, books),
    get: async () => await LocalStorage.get<Book[]>(key) || [],
    clear: () => LocalStorage.remove(key),
});

const RELATED_BOOKS_STORAGE_KEY = "related_books_storage";

export const RelatedBooksStorage = BooksStorage(RELATED_BOOKS_STORAGE_KEY);
