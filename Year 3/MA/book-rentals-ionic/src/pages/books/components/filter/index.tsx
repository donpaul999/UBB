import { MenuItem, Select, TextField } from "@mui/material";
import { observer } from "mobx-react";
import { createAnimation } from "@ionic/react";
import { WithDataProvider, withDataProvider } from "../../../../infrastructure";
import styles from "./filter.module.scss";
import {useEffect, useRef, useState} from "react";
import classNames from "classnames";

interface Props extends WithDataProvider {
    showAnimation: boolean;
}

const FilterBar = ({showAnimation, search, bookFilter, setSearch, setBookFilter }: Props) => {
    const elementReference = useRef<HTMLDivElement>(null);
    const [isInitialized, setInitialized] = useState(false);

    useEffect(() => {
        const playAnimation = (show = true) => {
            if (!elementReference.current)
                return;

            if (!isInitialized)
                return setInitialized(true);

            const animation = createAnimation()
                .addElement(elementReference.current)
                .keyframes([{
                    offset: 0,
                    maxHeight: 0,
                    opacity: 0
                }, {
                    offset: 0.5,
                    maxHeight: "5rem",
                    opacity: 1
                }, {
                    offset: 1,
                    maxHeight: "10rem",
                    opacity: 1
                }]).duration(show ? 3000 : 1000)
                .easing("ease-out");

            if (!show)
                animation.direction("reverse");
            animation.play();
        }
        playAnimation(showAnimation);
    }, [showAnimation]);

    const handleBookFilter = (value: string) => {
        if (value === "null") {
            return setBookFilter(null);
        }
        setBookFilter(value === "true");
    }

    const getSelectedValue = () => {
        if (bookFilter === null) {
            return "null";
        }
        return bookFilter.toString();
    }

    return (
        <div
            ref={elementReference}
            className={classNames(styles.filterBar, {
                [styles.showAnimation]: showAnimation,
            })}>
            <TextField
                label="Search"
                className={styles.input}
                value={search}
                variant="filled"
                size="small"
                onChange={e => setSearch(e.target.value)} />
            <Select
                value={getSelectedValue()}
                size="small"
                onChange={e => handleBookFilter(e.target.value as string)}>
                <MenuItem value="null">Show all</MenuItem>
                <MenuItem value="false">Show available only</MenuItem>
                <MenuItem value="true">Show booked only</MenuItem>
            </Select>
        </div>
    );
}

export default withDataProvider(observer(FilterBar));
