import { IonContent, IonImg, IonPage, IonTitle } from "@ionic/react";
import {Button, Fab, IconButton, Tab, Tabs} from "@mui/material";
import { Box } from "@mui/system";
import { useContext } from "react";
import SwipeableViews from "react-swipeable-views";
import AddIcon from '@mui/icons-material/AddSharp';
import styles from "./main-page.module.scss";
import { ToastService, WithDataProvider, withDataProvider } from "../../infrastructure";
import BookList from "./components/book-list";
import { MainPageContext } from "./main-page-store";
import BookEdit from "./components/book-edit";
import { observer } from "mobx-react";
import SignOutIcon from '@mui/icons-material/NoAccountsSharp';
import NetworkStatusMessage from "./components/network-status";

const MainPage = ({ allBooks, relatedBooks }: WithDataProvider) => {
    const {
        selectedTab,
        bookToEdit,

        setSelectedTab,
        showAddDialog,
        showEditDialog,
        closeDialog,
        signOut
    } = useContext(MainPageContext);

    return (
        <IonPage>
            <IonContent fullscreen>
                <div className={styles.pageContainer}>
                    <Box sx={{ borderBottom: 1, borderColor: "divider"}}>
                        <div className={styles.header}>
                            <IonTitle className={styles.applicationTitle}>My books</IonTitle>
                            <Button onClick={signOut}>Log out</Button>
                        </div>
                        <Tabs
                            variant="fullWidth"
                            value={selectedTab}
                            onChange={(_, tab) => setSelectedTab(tab)}>
                                <Tab label="My books" value={0} />
                        </Tabs>
                    </Box>
                    <NetworkStatusMessage />
                    <SwipeableViews
                        axis="x"
                        index={selectedTab}
                        onChangeIndex={setSelectedTab}>
                        <div
                            className={styles.tabPanel}
                            role="tabpanel"
                            hidden={selectedTab !== 0}>
                            <BookList
                                books={relatedBooks}
                                onClick={(book) => showEditDialog(book)}/>
                        </div>
                    </SwipeableViews>
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
