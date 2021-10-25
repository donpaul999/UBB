import { Book } from "../../accessors/types";

export type WebSocketListener = (book: Book) => void;
