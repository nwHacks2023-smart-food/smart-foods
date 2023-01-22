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
    const test = async () => {
        const response = await axios.get(
            'http://127.0.0.1:8000/api/nutrition?food=apple'
        );
        console.log(response.data);
    };

    return (
        <Layout>
            <div className={styles.container}>
                <h2 className={styles.step}>Step 1: Choose your foods</h2>
                <div className={styles.content}>
                    <div className={styles.input}>
                        <input
                            type="text"
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
                        <button
                            type="submit"
                            className={styles.addButton}
                            onClick={test}
                        >
                            +
                        </button>
                    </div>
                    <div className={styles.cards}>
                        <Card
                            imageSearch="PLACEHOLDER"
                            name="Orange"
                            mass="50g"
                            calories="200"
                            sugar="14g"
                            protein="2g"
                        />
                    </div>
                </div>
                <Button text="Next" path="/build_cart" />
            </div>
        </Layout>
    );
};

export default Choose;
