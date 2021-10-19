import { toJS } from "mobx"

export const addToList = <T>(list: T[], value: T): T[] => {
    const listWithValue = toJS(list);

    listWithValue.push(value);

    return listWithValue;
}

export const updateInList = <T>(list: T[], value: T, where: (element: T) => boolean): [T[], T | null] => {
    const indexToUpdate = list.findIndex(where);
    if (indexToUpdate < 0) {
        return [list, null];
    }

    const listWithUpdate = toJS(list);
    const bookToUpdate = listWithUpdate[indexToUpdate];
    listWithUpdate.splice(indexToUpdate, 1, value);

    return [listWithUpdate, bookToUpdate];
}

export const removeFromList = <T>(list: T[], which: (element: T) => boolean): T[] => {
    const indexToRemove = list.findIndex(which);
    if (indexToRemove < 0) {
        return list;
    }

    const listWithoutValue = toJS(list);
    listWithoutValue.splice(indexToRemove, 1);
    
    return listWithoutValue;
}
