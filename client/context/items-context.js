import { createContext, useState } from 'react';
export const ItemsContext = createContext({
    items: {},
});

export const ItemsProvider = ({ children }) => {
    const [items, setItems] = useState({});
    const value = { items, setItems };
    return (
        <ItemsContext.Provider value={value}>{children}</ItemsContext.Provider>
    );
};
