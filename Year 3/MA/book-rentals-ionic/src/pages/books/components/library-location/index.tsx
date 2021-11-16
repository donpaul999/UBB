import { AppBar, Button, Dialog, IconButton, Slide, Toolbar, Typography } from "@mui/material";
import { forwardRef, useContext, useEffect } from "react";
import CloseIcon from "@mui/icons-material/CloseSharp";
import Map from "./map";
import styles from "./library-location.module.scss";
import { LibraryLocationDialogContext } from "./library-location-store";
import { IonSpinner } from "@ionic/react";
import { observer } from "mobx-react";
import { toJS } from "mobx";
import IFrameMap from "./iframe-map";

// false - not working
const USE_EMBEDDED = true;

interface Props {
    isOpen: boolean;
    onClose: () => void;
}

const Transition = forwardRef(function Transition(props: any, ref) {
    return <Slide direction="right" ref={ref} {...props} />;
});

const LibraryLocationDialog = ({ isOpen, onClose }: Props) => {
    const {
        libraryLocation,
        loadLibraryLocation,
        reset,
        setLibraryLocation
    } = useContext(LibraryLocationDialogContext);

    useEffect(() => {
        if (isOpen) {
            loadLibraryLocation();

            return reset;
        }
    }, [loadLibraryLocation, reset, isOpen]);

    return (
        <Dialog
            fullScreen
            open={isOpen}
            onClose={onClose}
            TransitionComponent={Transition}>
            <AppBar
                sx={{ position: "relative" }}
                color="inherit">
                <Toolbar>
                    <Typography
                        sx={{
                            ml: 2,
                            flex: 1
                        }}
                        variant="h6"
                        color="black"
                        fontWeight="bold"
                        component="div">
                        Your book library location
                    </Typography>
                    <IconButton
                        onClick={onClose}
                        color="primary">
                        <CloseIcon />
                    </IconButton>
                </Toolbar>
            </AppBar>
            <div className={styles.container}>
                {libraryLocation && (
                    USE_EMBEDDED ? (
                        <IFrameMap {...libraryLocation} />
                    ) : (
                        <Map
                            googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyAIBbUmwHVhwjTxWXtKu_ROw1d9j-Of4bU&libraries=geometry,drawing,places"
                            mapElement={<div style={{ height: `100%`, width: "100%" }} />}
                            containerElement={<div style={{ height: `400px`, width: "100%" }} />}
                            loadingElement={<IonSpinner />}
                            {...libraryLocation} />
                    )
                )}
                <Button
                    color="secondary"
                    variant="outlined"
                    onClick={setLibraryLocation}>
                    Set current location
                </Button>
            </div>
        </Dialog>
    );
}

export default observer(LibraryLocationDialog);
