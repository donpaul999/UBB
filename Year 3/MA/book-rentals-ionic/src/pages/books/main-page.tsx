import {IonContent, IonInfiniteScroll, IonInfiniteScrollContent, IonPage, IonTitle} from "@ionic/react";
import {Button, Fab, IconButton, Tab, Tabs} from "@mui/material";
import { Box } from "@mui/system";
import { useContext } from "react";
import AddIcon from '@mui/icons-material/AddSharp';
import styles from "./main-page.module.scss";
import { ToastService, WithDataProvider, withDataProvider } from "../../infrastructure";
import BookList from "./components/book-list";
import { MainPageContext } from "./main-page-store";
import BookEdit from "./components/book-edit";
import { observer } from "mobx-react";
import NetworkStatusMessage from "./components/network-status";
import {Logout} from "@mui/icons-material";
import FilterBar from "./components/filter";

const MainPage = ({ relatedBooks, disabledScroll, fetchRelatedBooks }: WithDataProvider) => {
    const {
        bookToEdit,
        showAddDialog,
        showEditDialog,
        closeDialog,
        signOut
    } = useContext(MainPageContext);

    const handleOnScroll = async (event: any) => {
        await fetchRelatedBooks();

        event.target.complete();
    }

    return (
        <IonPage>
            <IonContent fullscreen>
                <div className={styles.pageContainer}>
                    <Box sx={{ borderBottom: 1, borderColor: "divider"}}>
                        <div className={styles.header}>
                            <IonTitle className={styles.applicationTitle}>My books</IonTitle>
                            <Button onClick={signOut}><Logout color="primary" /></Button>
                        </div>
                    </Box>
                    <NetworkStatusMessage />
                    <FilterBar/>
                    <BookList books={relatedBooks} onClick={(book) => showEditDialog(book)}/>
                    <IonInfiniteScroll
                        disabled={disabledScroll}
                        onIonInfinite={e => handleOnScroll(e as any)}>
                        <IonInfiniteScrollContent />
                    </IonInfiniteScroll>
                    <Fab
                        className={styles.addButton}
                        onClick={() => showAddDialog()}>
                        <AddIcon color="primary" />
                    </Fab>
                    <ToastService />
                    <BookEdit
                        initialBook={bookToEdit}
                        onClose={closeDialog} />
                </div>
            </IonContent>
        </IonPage>
    );
}

export default withDataProvider(observer(MainPage));
