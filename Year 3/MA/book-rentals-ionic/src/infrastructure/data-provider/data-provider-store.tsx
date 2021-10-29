import { makeAutoObservable, runInAction } from "mobx";
import { createContext } from "react";
import { authorizedStore, BuildWebSocket, toastServiceStore } from "..";
import {
    addBook,
    deleteBook,
    getRelatedBooks, syncChanges,
    updateBook
} from "../../accessors/book-accessor";
import { Book } from "../../accessors/types";
import { addToList, removeFromList, updateInList } from "../../shared/array-helpers";
import {networkStatusStore} from "../network-status/network-status-store";
import OfflineBookAccessor from "../../accessors/book-accessor-offline";

const PAGINATION_COUNT = 4;

export class DataProviderStore {
    public allBooks: Book[] = []
    public relatedBooks: Book[] = []
    private isInitialized = false
    public disabledScroll: boolean = false;
    public search: string = "";
    public bookFilter: boolean | null = null;
    private unsubscribe = () => {};
    private start = 0;

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

        networkStatusStore.onConnectionChange = connected => {
            if (connected)
                syncChanges();
        }
        this.getBooks();
        return this.subscribeToChanges();
    }

    private getBooks = () => setTimeout(() => {
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

    private getRelatedBooks = async () => {
        this.start = 0;
        this.relatedBooks = [];
        this.disabledScroll = false;
        await this.fetchRelatedBooks();
    }

    public fetchRelatedBooks = async () => {
        const relatedCars = await getRelatedBooks(
            this.search,
            this.bookFilter,
            this.start,
            PAGINATION_COUNT);

        runInAction(() => {
            this.start += PAGINATION_COUNT;
            this.disabledScroll = relatedCars.length < PAGINATION_COUNT;
            this.relatedBooks.push(...relatedCars);
        });
    }

    public setSearch = (search: string) => {
        this.search = search;
        this.getRelatedBooks();
    }

    public setBookFilter = (isBooked: boolean | null) => {
        this.bookFilter = isBooked;
        this.getRelatedBooks();
    }

    private handleCreateChange = (book: Book) => {
        if (book.userId === authorizedStore.userId) {
            this.relatedBooks = addToList(this.relatedBooks, book);
            this.addToRelatedBooks(book);
            OfflineBookAccessor.addBook(book);
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
            this.updateInRelatedBooks(book);
            OfflineBookAccessor.updateBook(book);
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
            this.deleteFromRelatedBooks(book);
            OfflineBookAccessor.deleteBook(book.id);
        } else {
            this.allBooks = removeFromList(this.allBooks, ({ id }) => book.id === id);
        }

        toastServiceStore.showInfo(<>
            The book&nbsp;<strong>{book.name} by {book.author}</strong>&nbsp;was removed from the list
        </>);
    }

    public updateInRelatedBooks = (book: Book) => {
        const [updatedList, bookToUpdate] =
            updateInList(this.relatedBooks, book, ({ id }) => book.id === id);
        if (!bookToUpdate) {
            return;
        }
        this.relatedBooks = updatedList;
    }

    public addToRelatedBooks = (book: Book) => this.relatedBooks = addToList(this.relatedBooks, book);

    public deleteFromRelatedBooks = (book: Book) =>
        this.relatedBooks = removeFromList(this.relatedBooks, ({ id }) => book.id === id);
}

export const dataProviderStore = new DataProviderStore();
export const DataProviderContext = createContext(dataProviderStore);
