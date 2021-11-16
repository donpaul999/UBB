import { LibraryLocation } from "./types";
import { API_PATH_LIBRARY_LOCATION, BASE_HTTP_URL } from "./constants";
import { httpGet, httpPost } from "./helper-functions";

const BASE_LIBRARY_LOCATION_URL = BASE_HTTP_URL + API_PATH_LIBRARY_LOCATION;

export const getLibraryLocation = async () => {
    try {
        return await httpGet<LibraryLocation>(BASE_LIBRARY_LOCATION_URL);
    } catch {
        return null;
    }
}

export const setLibraryLocation = (libraryLocation: LibraryLocation) =>
    httpPost(BASE_LIBRARY_LOCATION_URL, libraryLocation);
