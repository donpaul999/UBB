import { makeAutoObservable, runInAction, toJS } from "mobx";
import { createContext } from "react";
import { Book, EMPTY_BOOK } from "../../../../accessors/types";
import {
    Camera,
    CameraResultType,
    CameraSource
  } from "@capacitor/camera";
import { addBook, deleteBook, updateBook } from "../../../../accessors/book-accessor";
import {AuthenticationStorage, toastServiceStore} from "../../../../infrastructure";
import {dataProviderStore} from "../../../../infrastructure/data-provider/data-provider-store";

export class BookEditStore {
    public book: Book = EMPTY_BOOK;
    public isAdd: boolean = false;
    public showCloseConfirmation: boolean = false;
    public showDeleteConfirmation: boolean = false;

    constructor() {
        makeAutoObservable(this);
    }

    public initializeBook = (initialBook: Book | null) => {
        if (!initialBook) {
            return;
        }

        if (initialBook.id === 0) {
            this.isAdd = true;
            this.book = EMPTY_BOOK;
            return;
        }

        this.isAdd = false;
        this.book = toJS(initialBook);
    }

    public setName = (name: string) => this.book.name = name;

    public setAuthor = (author: string) => this.book.author = author;

    public setPublishDate = (publishDate: string) =>
        this.book.publishDate = publishDate;

    public setBooked = (isBooked: boolean) => this.book.isBooked = isBooked ? "true" : "false";

    public canSave = () => this.book.name && this.book.author &&
        this.book.publishDate;

    public saveBook = async () => {
        const api = this.isAdd ? addBook : updateBook;

        try {
            const online = await api(this.book);

            if (online) {
                toastServiceStore.showSuccess("Operation successful!");
            } else {
                const saveMethod = this.isAdd ? dataProviderStore.addToRelatedBooks :
                    dataProviderStore.updateInRelatedBooks;

                saveMethod(this.book);
                toastServiceStore.showWarning("Book saved to local storage!");
            }
        } catch {
            toastServiceStore.showError("Something went wrong, the server could not save the book, try again!");
            return false;
        }
        
        toastServiceStore.showSuccess("Operation successful!");
        return true;
    }

    public takePicture = async () => {
        const cameraPhoto = await Camera.getPhoto({
            resultType: CameraResultType.Base64,
            source: CameraSource.Camera,
            quality: 100
        });
        runInAction(() => {
            this.book.image = cameraPhoto.base64String ?? "";
        });
    }

    public deleteBook = async () => {
        try {
            const online = await deleteBook(this.book.id);

            if (online) {
                toastServiceStore.showSuccess("Operation successful!");
            } else {
                dataProviderStore.deleteFromRelatedBooks(this.book);
                toastServiceStore.showWarning("Book removed in local storage!");
            }
        } catch {
            toastServiceStore.showError("Something went wrong, the server could not delete the book, try again!");
            return false;
        }

        toastServiceStore.showSuccess("Operation successful!");
        return true;
    }

    public setCloseConfirmation = (show: boolean) => this.showCloseConfirmation = show;

    public setDeleteConfirmation = (show: boolean) => this.showDeleteConfirmation = show;
}

export const bookEditStore = new BookEditStore();
export const BookEditContext = createContext(bookEditStore);