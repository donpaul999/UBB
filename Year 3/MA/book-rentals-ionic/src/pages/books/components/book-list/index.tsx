import { IonCard } from "@ionic/react";
import { Book } from "../../../../accessors/types";
import { ByteImage } from "../../../../components";
import styles from "./book-list.module.scss";

interface Props {
    books: Book[]
    onClick?: (book: Book) => void;
}

const BookList = ({ books, onClick }: Props) => {
    return <>
        {books?.length ? books.map(book => (
            <IonCard
                key={book.id}
                className={styles.itemContainer}
                onClick={() => onClick && onClick(book)}>
                <ByteImage byteSrc={book.image} />
                <div className={styles.itemDetails}>
                    <div className={styles.row}>
                        <div>
                            <strong>Name:</strong> {book.name}
                        </div>
                        <div>
                            <strong>Author:</strong> {book.author}
                        </div>
                    </div>
                    <div className={styles.row}>
                        <div>
                            <strong>Id:</strong> {book.id}
                        </div>
                        <div>
                            <strong>Publish date:</strong> {book.publishDate}
                        </div>
                    </div>
                    <div className={styles.row}>
                        <div>
                            <strong>Is it available?</strong> {!book.isBooked ? "Yes" : "No"}
                        </div>
                    </div>
                </div>
            </IonCard>
        )) : (
            <div className={styles.notFound}>No books found...</div>
        )}
    </>
}

export default BookList;
