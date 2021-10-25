import { makeAutoObservable, runInAction } from "mobx";
import { createContext } from "react";
import { authorizedStore, BuildWebSocket, toastServiceStore } from "..";
import {
    addBook,
    deleteBook, getAllBooks,
    getRelatedBooks,
    updateBook
} from "../../accessors/book-accessor-online";
import { Book } from "../../accessors/types";
import { addToList, removeFromList, updateInList } from "../../shared/array-helpers";

export class DataProviderStore {
    public allBooks: Book[] = []
    public relatedBooks: Book[] = []
    private isInitialized = false
    private unsubscribe = () => {};

    constructor() {
        makeAutoObservable(this);
    }

    public addBook = async (book: Book) => addBook(book);

    public updateBook = async (book: Book) => updateBook(book);

    public deleteBook = (book: Book) => deleteBook(book.id);

    initialize = () => {
        if (this.isInitialized) {
            return () => {};
        }

        this.isInitialized = true;
        return this.getBooks();
    }

    private getBooks = () => setTimeout(() => {
        this.getAvailableBooks();
        this.getRelatedBooks();
        return this.subscribeToChanges();
    }, 100);

    private subscribeToChanges = async () => {
        const unsubscribe = await BuildWebSocket()
            .onCreate(this.handleCreateChange)
            .onUpdate(this.handleUpdateChange)
            .onDelete(this.handleDeleteChange)
            .connect();

        runInAction(() => this.unsubscribe = unsubscribe);
    }

    public unsubscribeToChanges = () => {
        try {
            this.unsubscribe();
        } catch {}
    }

    private getAvailableBooks = async () => {
        const allBooks = await getAllBooks();
        runInAction(() => {
            this.allBooks = allBooks;
        });
    }

    private getRelatedBooks = async () => {
        const relatedBooks = await getRelatedBooks();
        runInAction(() => {
            this.relatedBooks = relatedBooks;
        });
    }

    private handleCreateChange = (book: Book) => {
        if (book.userId === authorizedStore.userId) {
            this.relatedBooks = addToList(this.relatedBooks, book);
        } else {
            this.allBooks = addToList(this.allBooks, book);
        }

        toastServiceStore.showInfo(<>
            New book (<strong>{book.name} by {book.author}</strong>) added to the list
        </>);
    }

    private handleUpdateChange = (book: Book) => {
        const isRelated = book.userId === authorizedStore.userId;
        const [updatedList, bookToUpdate] = updateInList(
            isRelated ? this.relatedBooks : this.allBooks,
            book,
            ({ id }) => book.id === id);
        if (!bookToUpdate) {
            return;
        }

        if (isRelated) {
            this.relatedBooks = updatedList;
        } else {
            this.allBooks = updatedList;
        }

        let newName = <></>;
        if (bookToUpdate.name !== book.name) {
            newName = <>&nbsp;to&nbsp;<strong>{book.name}</strong></>;
        }

        toastServiceStore.showInfo(<>
            The book&nbsp;<strong>{bookToUpdate.name} by {bookToUpdate.author}</strong>&nbsp;was updated - {newName}
        </>);
    }

    private handleDeleteChange = (book: Book) => {
        if (book.userId === authorizedStore.userId) {
            this.relatedBooks = removeFromList(this.relatedBooks, ({ id }) => book.id === id);
        } else {
            this.allBooks = removeFromList(this.allBooks, ({ id }) => book.id === id);
        }

        toastServiceStore.showInfo(<>
            The book&nbsp;<strong>{book.name} by {book.author}</strong>&nbsp;was removed from the list
        </>);
    }
}

export const dataProviderStore = new DataProviderStore();
export const DataProviderContext = createContext(dataProviderStore);
