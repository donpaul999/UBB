import { IonContent, IonPage, IonTitle } from "@ionic/react";
import { Alert, AlertTitle, Button, IconButton, TextField } from "@mui/material";
import classNames from "classnames";
import { observer } from "mobx-react";
import ArrowBack from "@mui/icons-material/ArrowBackSharp";
import styles from "./register.module.scss";
import { useContext, useEffect } from "react";
import { RegisterContext } from "./register-store";
import { useHistory } from "react-router";

const Register = () => {
    const { push } = useHistory();

    const {
        user,
        errorMessage,
        successMessage,
        setEmail,
        setPassword,
        setConfirmPassword,
        register,
        reset
    } = useContext(RegisterContext);

    useEffect(() => {
        return reset;
    }, []);

    const arePasswordsDifferent = user.password !== user.confirmPassword;

    return (
        <IonPage>
            <IonContent fullscreen>
                <div className={styles.mainContainer}>
                    <div className={styles.centeredContainer}>
                        <div className={classNames(styles.row, styles.largeText)}>
                            <IonTitle className={styles.applicationTitle}>My books</IonTitle>
                        </div>
                        <IonTitle className={classNames(styles.logInText, styles.largeText)}>
                            Register
                        </IonTitle>
                        <TextField
                            label="Email"
                            type="email"
                            className={styles.inputEmail}
                            value={user.email}
                            onChange={e => setEmail(e.target.value)} />
                        <TextField
                            label="Password"
                            type="password"
                            helperText="Password shall contain a small letter, a capital letter, a digit and a special symbol."
                            className={styles.inputPassword}
                            value={user.password}
                            onChange={e => setPassword(e.target.value)} />
                        <TextField
                            label="Confirm password"
                            type="password"
                            className={styles.inputPassword}
                            value={user.confirmPassword}
                            helperText={arePasswordsDifferent && "The passwords are different!"}
                            error={arePasswordsDifferent}
                            onChange={e => setConfirmPassword(e.target.value)} />
                        {errorMessage && (
                            <Alert
                                severity="error"
                                className={styles.alertContainer}>
                                <AlertTitle><strong>Error</strong></AlertTitle>
                                {errorMessage}
                            </Alert>
                        )}
                        {successMessage && (
                            <Alert
                                severity="success"
                                className={styles.alertContainer}>
                                <AlertTitle><strong>Success!</strong></AlertTitle>
                                {successMessage}
                            </Alert>
                        )}
                        <div className={classNames(styles.row)}>
                            <Button
                                className={styles.registerButton}
                                onClick={() => push("/login")}>
                                Log in
                            </Button>
                            <Button
                                variant="contained"
                                color="secondary"
                                className={styles.registerButton}
                                disabled={!user.email || !user.password || !user.confirmPassword}
                                onClick={register}>
                                Create account
                            </Button>
                        </div>
                    </div>
                </div>
            </IonContent>
        </IonPage>
    );
}

export default observer(Register);
