import { useEffect, useState } from 'react';
import axios from 'axios';
import styles from './Image.module.css';

const Image = ({ queryParam }) => {
    const [result, setResult] = useState('');

    useEffect(() => {
        async function fetchData() {
            const result = await axios.get(
                `https://www.googleapis.com/customsearch/v1?key=AIzaSyAnRA9N5OBTAKqb8sScaegM-YPyriTpByQ&cx=655d6cda3a6114be9&q=${queryParam}+food&searchType=image&start=1&num=1`
            );

            setResult(result);
        }
        fetchData();
    }, []);

    return (
        <img
            className={styles.image}
            src={result && result.data.items[0].link}
            alt={queryParam}
        />
    );

    // return <img className={styles.image} src="favicon.ico" alt="Placholder image -- need new Google API key" />
};

export default Image;
