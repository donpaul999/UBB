import { LocalStorage } from "..";
import { Book, Change, ChangeType, EMPTY_BOOK } from "../../accessors/types";

const SYNC_BOOKS_STORAGE_KEY = "sync_books_storage";

const queueCreate = async (book: Book) => {
    const queue = await LocalStorage.get<Change[]>(SYNC_BOOKS_STORAGE_KEY) || [];

    queue.push({
        type: ChangeType.Create,
        payload: book
    });

    await LocalStorage.set(SYNC_BOOKS_STORAGE_KEY, queue);
}

const queueUpdate = async (book: Book) => {
    const queue = await LocalStorage.get<Change[]>(SYNC_BOOKS_STORAGE_KEY) || [];

    queue.push({
        type: ChangeType.Update,
        payload: book
    });

    await LocalStorage.set(SYNC_BOOKS_STORAGE_KEY, queue);
}

const queueDelete = async (bookId: number) => {
    console.log("sync offline del!");

    let queue = await LocalStorage.get<Change[]>(SYNC_BOOKS_STORAGE_KEY) || [];
    console.log("sync offline del2!");

    if (bookId > 0) {
        queue.push({
            type: ChangeType.Delete,
            payload: {
                ...EMPTY_BOOK,
                id: bookId
            }
        })
        console.log(queue);
        console.log("sync offline del4!");
    } else {
        queue = queue.filter(({ payload }) => payload.id !== bookId);
    }

    console.log("sync offline del6!");
    await LocalStorage.set(SYNC_BOOKS_STORAGE_KEY, queue);
}

const getChanges = async () => {
    const queue = await LocalStorage.get<Change[]>(SYNC_BOOKS_STORAGE_KEY) || [];
    await LocalStorage.remove(SYNC_BOOKS_STORAGE_KEY);

    return queue;
}

export default {
    queueCreate,
    queueUpdate,
    queueDelete,
    getChanges
};
