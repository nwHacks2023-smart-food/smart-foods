import { useState, useEffect, useContext } from 'react';
import { ItemsContext } from '../context/items-context.js';
import axios from 'axios';
import Layout from '../components/Layout/Layout';
import styles from '../styles/build_cart.module.css';
import Button from '../components/Button/Button';
import Card2 from '../components/Card2/Card2';
import Card3 from '../components/Card3/Card3';

const BuildCart = () => {
    const { items, setItems } = useContext(ItemsContext);
    const [itemsToCompare, setItemsToCompare] = useState({});
    // On items change, store it is local storage
    useEffect(() => {
        const getItemsData = async () => {
            const response = await axios.post(
                'http://localhost:8000/api/items',
                {
                    items: Object.keys(items),
                }
            );

            Object.keys(items).forEach((key) =>
                setItemsToCompare({
                    ...itemsToCompare,
                    [key]: {
                        amazon: response.data.amazon[key],
                        saveonfood: response.data.saveonfood[key],
                    },
                })
            );
        };
        getItemsData();
    }, []);
    return (
        <Layout>
            <div className={styles.container}>
                <h2 className={styles.step}>Step 2: Build your cart</h2>
                <section>
                    <div className={styles.content}>
                        <div className={styles.cards}>
                            <h3>Compare</h3>
                            {Object.keys(itemsToCompare)?.map((key) => {
                                const itemsByWebsite = itemsToCompare[key];
                                return (
                                    <>
                                        <h4>{key}</h4>
                                        <Card2
                                            key={itemsByWebsite.amazon.link}
                                            imageSearch={items[key].imageSearch}
                                            mass={items[key].mass}
                                            price={itemsByWebsite.amazon.price}
                                            website={itemsByWebsite.amazon.link}
                                        ></Card2>
                                        <Card2
                                            key={itemsByWebsite.saveonfood.link}
                                            imageSearch={items[key].imageSearch}
                                            mass={items[key].mass}
                                            price={
                                                itemsByWebsite.saveonfood.price
                                            }
                                            website={
                                                itemsByWebsite.saveonfood.link
                                            }
                                        ></Card2>
                                    </>
                                );
                            })}
                            {/* <Card2
                                imageSearch=""
                                name="Orange"
                                mass="50g"
                                price="$3.22"
                                website="www.amazon.com"
                            /> */}
                        </div>
                    </div>
                    <div className={styles.content}>
                        <div className={styles.cards}>
                            <h3>Cart</h3>
                            <Card3
                                imageSearch=""
                                name="Orange"
                                mass="50g"
                                price="$3.22"
                                website="www.amazon.com"
                            />
                        </div>
                    </div>
                </section>

                <div className={styles.buttons}>
                    <Button text="Go Back" path="/choose" />
                    <Button text="View Summary" path="/build_cart" />
                </div>
            </div>
        </Layout>
    );
};

export default BuildCart;
