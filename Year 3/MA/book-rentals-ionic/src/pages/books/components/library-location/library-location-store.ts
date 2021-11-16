import { createContext } from "react";
import { getLibraryLocation, setLibraryLocation } from "../../../../accessors/library-location-accessor";
import { LibraryLocation } from "../../../../accessors/types";
import { Geolocation } from "@capacitor/geolocation";
import { makeAutoObservable, runInAction } from "mobx";

export class LibraryLocationDialogStore {
    public libraryLocation: LibraryLocation | null = null;

    constructor() {
        makeAutoObservable(this);
    }

    public loadLibraryLocation = async () => {
        const libraryLocation = await getLibraryLocation();
        runInAction(() => this.libraryLocation = libraryLocation);
    }

    public setLibraryLocation = async () => {
        const { coords: { latitude, longitude } } = await Geolocation.getCurrentPosition();
        const libraryLocation = {
            latitude,
            longitude
        };
        await setLibraryLocation(libraryLocation);
        runInAction(() => this.libraryLocation = libraryLocation);
    }

    public reset = () => {
        this.libraryLocation = null;
    }
}

export const libraryLocationDialogStore = new LibraryLocationDialogStore();
export const LibraryLocationDialogContext = createContext(libraryLocationDialogStore);
