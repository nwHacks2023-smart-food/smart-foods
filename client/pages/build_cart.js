<<<<<<< HEAD
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
            const response = await axios.post('/api/items', {
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Private-Network': true,
                    'Access-Control-Allow-Credentials': 'true',
                },
                items: Object.keys(items),
            });
=======
import { useState, useEffect, useContext } from "react";
import { ItemsContext } from "../context/items-context.js";
import axios from "axios";
import Layout from "../components/Layout/Layout";
import styles from "../styles/build_cart.module.css";
import Button from "../components/Button/Button";
import Card2 from "../components/Card2/Card2";

const BuildCart = () => {
	const { items, setItems } = useContext(ItemsContext);
	const [itemsToCompare, setItemsToCompare] = useState({});
	const [cartItems, setCartItems] = useState([]);
	// On items change, store it is local storage
	useEffect(() => {
		const getItemsData = async () => {
			const response = await axios.post("http://localhost:8000/api/items", {
				items: Object.keys(items),
			});
>>>>>>> 9f1b0b6d8ecd4e3d739fbd75e4258a9b9b5bfe62

            Object.keys(items).forEach((key) => {
                setItemsToCompare((prevVals) => ({
                    ...prevVals,
                    [key]: {
                        amazon: response.data.amazon[key],
                        saveonfood: response.data.saveonfood[key],
                    },
                }));
            });
        };
        getItemsData();
    }, []);

<<<<<<< HEAD
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
                                console.log(key);
                                return (
                                    <>
                                        <Card2
                                            name={key}
                                            key={itemsByWebsite.amazon.link}
                                            imageSearch={items[key].imageSearch}
                                            mass={items[key].mass}
                                            price={itemsByWebsite.amazon.price}
                                            website={itemsByWebsite.amazon.link}
                                        ></Card2>
                                        <Card2
                                            name={key}
                                            key={itemsByWebsite.saveonfood.link}
                                            imageSearch={items[key].imageSearch}
                                            mass={items[key].mass}
                                            price={
                                                itemsByWebsite.saveonfood?.price
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
=======
	function handleAddProduct(data) {
		setCartItems((prev) => [...prev, data]);
	}

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
								console.log(key);
								return (
									<>
										<Card2
											name={key}
											key={itemsByWebsite.amazon.link}
											imageSearch={items[key].imageSearch}
											mass={items[key].mass}
											price={itemsByWebsite.amazon.price}
											website={itemsByWebsite.amazon.link}
											buttonHandler={handleAddProduct}
										></Card2>
										<Card2
											name={key}
											key={itemsByWebsite.saveonfood?.link}
											imageSearch={items[key].imageSearch}
											mass={items[key].mass}
											price={itemsByWebsite.saveonfood?.price}
											website={itemsByWebsite.saveonfood?.link}
											buttonHandler={handleAddProduct}
										></Card2>
									</>
								);
							})}
						</div>
					</div>
					<div className={styles.content}>
						<div className={styles.cards}>
							<h3>Cart</h3>
							{cartItems.map((item) => {
								return (
									<Card2
										imageSearch={item.imageSearch}
										name={item.name}
										mass={item.mass}
										price={item.price}
										website={item.website}
										noAdd={true}
									/>
								);
							})}
						</div>
					</div>
				</section>

				<div className={styles.buttons}>
					<Button text="Go Back" path="/choose" />
				</div>
			</div>
		</Layout>
	);
>>>>>>> 9f1b0b6d8ecd4e3d739fbd75e4258a9b9b5bfe62
};

export default BuildCart;
