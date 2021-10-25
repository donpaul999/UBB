import { SyncStorage } from "../infrastructure";
import { networkStatusStore } from "../infrastructure/network-status/network-status-store";
import OfflineBookAccessor from "./book-accessor-offline";
import OnlineBookAccessor from "./book-accessor-online";
import { Book } from "./types";

export const getRelatedBooks = async () => {
    if (!isOnline()) {
        return OfflineBookAccessor.getRelatedBooks();
    }

    const books = await OnlineBookAccessor.getRelatedBooks();
    await OfflineBookAccessor.setRelatedBooks(books);
    return books;
}

export const addBook = async (book: Book) => {
    if (isOnline()) {
        await OnlineBookAccessor.addBook(book);
        return true;
    }

    await SyncStorage.queueCreate(book);
    await OfflineBookAccessor.addBook(book);
    return false;
}

export const updateBook = async (book: Book) => {
    if (isOnline()) {
        await OnlineBookAccessor.updateBook(book);
        return true;
    }

    await SyncStorage.queueUpdate(book);
    await OfflineBookAccessor.updateBook(book);
    return false;
}

export const deleteBook = async (bookId: number) => {
    if (isOnline()) {
        await OnlineBookAccessor.deleteBook(bookId);
        return true;
    }

    await SyncStorage.queueDelete(bookId);
    await OfflineBookAccessor.deleteBook(bookId);
    return false;
}

export const syncChanges = async () => {
    const changes = await SyncStorage.getChanges();
    if (!changes?.length) {
        return;
    }

    const idMapping = await OnlineBookAccessor.syncChanges(changes);
    await OfflineBookAccessor.updateIds(idMapping);
}

const isOnline = () => networkStatusStore.isConnected;
