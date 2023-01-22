import styles from './Card2.module.css';
import Image from '../Image/Image';

const Card2 = ({ imageSearch, name, mass, price, website }) => {
    return (
        <div className={styles.container}>
            <div className={styles.image}>
                <Image queryParam={imageSearch} />
            </div>
            <div className={styles.name_block}>
                <p className={styles.name}>{name}</p>
                <p className={styles.mass}>{mass}</p>
            </div>
            <div className={styles.choices}>
                <p className={styles.price}>{price}</p>
                <a className={styles.website} href={website}>
                    see product
                </a>
            </div>
        </div>
    );
};

export default Card2;
