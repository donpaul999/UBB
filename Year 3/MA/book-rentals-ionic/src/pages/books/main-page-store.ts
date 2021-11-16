import { makeAutoObservable } from "mobx";
import { createContext } from "react";
import { Book, EMPTY_BOOK } from "../../accessors/types";
import {authorizedStore, AuthenticationStorage, RelatedBooksStorage} from "../../infrastructure";
import {BooksStorage} from "../../infrastructure/local-storage/books-storage";

export class MainPageStore {
    public selectedTab: number = 0;
    public bookToEdit: Book | null = null;
    public showLibraryLocationDialog: boolean = false;
    public showAnimation: boolean = true;
    constructor() {
        makeAutoObservable(this);
    }

    public showAddDialog = () => this.bookToEdit = EMPTY_BOOK;

    public closeAddDialog = () => {
        this.bookToEdit = null;
        this.showAnimation = true
    };

    public showEditDialog = (book: Book) => {
        this.bookToEdit = book;
        this.showAnimation = false;
    }

    public openLibraryLocationDialog = () => {
        this.showLibraryLocationDialog = true;
        this.showAnimation = false;
    }

    public closeLibraryLocationDialog = () => {
        this.showLibraryLocationDialog = false;
        this.showAnimation = true
    }

    public signOut = async () => {
        await AuthenticationStorage.clear();
        await RelatedBooksStorage.clear();
        await authorizedStore.checkAuthorization();
    }
}

export const mainPageStore = new MainPageStore();
export const MainPageContext = createContext(mainPageStore);
