import { useState, useEffect } from 'react';
import Layout from '../components/Layout/Layout.js';
import styles from '../styles/choose.module.css';
import Button from '../components/Button/Button';
import Card from '../components/Card/Card';
import axios from 'axios';

const foodItems = [
    'apple',
    'banana',
    'orange',
    'strawberry',
    'grapes',
    'watermelon',
    'mango',
    'pear',
    'peach',
    'pineapple',
    'kiwi',
    'lemon',
    'lime',
    'blueberries',
    'raspberries',
    'blackberries',
    'cranberries',
    'strawberries',
    'broccoli',
    'carrots',
    'cauliflower',
    'celery',
    'cucumber',
    'eggplant',
    'garlic',
    'green beans',
    'onions',
    'peppers',
    'potatoes',
    'spinach',
    'tomatoes',
    'beef',
    'chicken',
    'pork',
    'lamb',
    'fish',
    'shrimp',
    'crab',
    'clams',
    'oysters',
    'scallops',
    'cod',
    'tuna',
    'salmon',
    'sardines',
    'trout',
    'lobster',
    'mussels',
    'abalone',
    'squid',
    'octopus',
    'bacon',
    'sausage',
    'ham',
    'prosciutto',
    'pasta',
    'rice',
    'bread',
    'croissant',
    'bagel',
    'muffin',
    'pancake',
    'waffle',
    'omelette',
    'quiche',
    'frittata',
    'scrambled eggs',
    'poached eggs',
    'hard-boiled eggs',
    'soft-boiled eggs',
    'custard',
    'yogurt',
    'ice cream',
    'sorbet',
    'gelato',
    'popsicle',
    'candy',
    'chocolate',
    'caramel',
    'fudge',
    'toffee',
    'taffy',
    'lollipop',
    'gummies',
    'marshmallows',
    'licorice',
    'jelly beans',
    'peanut butter',
    'almonds',
    'pecans',
    'walnuts',
    'cashews',
    'pistachios',
    'macadamia nuts',
    'brazil nuts',
    'hazelnuts',
    'pine nuts',
    'sunflower seeds',
    'pumpkin seeds',
    'sesame seeds',
    'chia seeds',
    'flax seeds',
    'hemp seeds',
    'poppy seeds',
];

const Choose = () => {
    const [items, setItems] = useState([]);
    // On items change, store it is local storage

    useEffect(() => {
        const items = JSON.parse(localStorage.getItem('items'));
        if (items) {
            setItems(items);
        }
    }, []);

    useEffect(() => {
        localStorage.setItem('items', JSON.stringify(items));
    }, [items]);

    const test = async (event) => {
        const itemName = event.target.food.value;
        event.preventDefault();
        const found = items.find((item) => item.name === itemName);
        if (found) {
            return;
        }
        const response = await axios.get(
            `http://127.0.0.1:8000/api/nutrition?food=${itemName}`
        );

        const { nf_calories, nf_sugars, nf_protein, nf_serving_weight_grams } =
            response.data[itemName];

        setItems([
            ...items,
            {
                imageSearch: itemName,
                name: itemName,
                mass: nf_serving_weight_grams,
                calories: nf_calories,
                sugar: nf_sugars,
                protein: nf_protein,
            },
        ]);
    };

    return (
        <Layout>
            <div className={styles.container}>
                <h2 className={styles.step}>Step 1: Choose your foods</h2>
                <div className={styles.content}>
                    <form className={styles.input} onSubmit={test}>
                        <input
                            type="text"
                            name="food"
                            placeholder="Enter a food:"
                            list="food-items"
                        />
                        <datalist id="food-items">
                            {foodItems.map((foodItem, index) => {
                                return (
                                    <option key={index} value={foodItem}>
                                        {foodItem}
                                    </option>
                                );
                            })}
                        </datalist>
                        <button type="submit" className={styles.addButton}>
                            +
                        </button>
                    </form>
                    <div className={styles.cards}>
                        {items?.map((item, index) => {
                            return <Card key={index} {...item} />;
                        })}
                    </div>
                </div>
                <Button text="Next" path="/build_cart" />
            </div>
        </Layout>
    );
};

export default Choose;
