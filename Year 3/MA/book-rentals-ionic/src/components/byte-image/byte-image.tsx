import { IonImg } from "@ionic/react";
import styles from "./byte-image.module.scss";
import DefaultImg from "../../shared/default-img";

interface Props {
    byteSrc: string;
}

const ByteImage = ({ byteSrc }: Props) => (
    <IonImg src={byteSrc ? `data:image/png;base64,${byteSrc}` : DefaultImg} className={styles.img} draggable="false" />
);

export default ByteImage;
