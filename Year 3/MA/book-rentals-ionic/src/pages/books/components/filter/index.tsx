import { MenuItem, Select, TextField } from "@mui/material";
import { observer } from "mobx-react";
import { WithDataProvider, withDataProvider } from "../../../../infrastructure";
import styles from "./filter.module.scss";

interface Props extends WithDataProvider {
}

const FilterBar = ({ search, bookFilter, setSearch, setBookFilter }: Props) => {
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
        <div className={styles.filterBar}>
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
