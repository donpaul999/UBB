export interface LoginUser {
    email: string;
    password: string;
}

export interface RegisterUser extends LoginUser {
    confirmPassword: string;
}

export interface LoginResponse {
    id: string;
    token: string;
    expiration: string;
}

export const EMPTY_LOGIN_USER: LoginUser = {
    email: "",
    password: ""
}

export const EMPTY_REGISTER_USER: RegisterUser = {
    ...EMPTY_LOGIN_USER,
    confirmPassword: ""
}

export interface Book {
    id: number;
    name: string;
    author: string;
    publishDate: string;
    isBooked: string;
    userId?: string;
    image: string;
}

export const EMPTY_BOOK: Book = {
    id: 0,
    name: "",
    author: "",
    publishDate: "0000-00-00",
    isBooked: "false",
    image: ""
}

export enum ChangeType {
    Create = 0,
    Update = 1,
    Delete = 2
}

export interface Change {
    type: ChangeType;
    payload: Book;
}

export interface IdMap {
    from: number;
    to: number;
}

export interface LibraryLocation {
    latitude: number;
    longitude: number;
}