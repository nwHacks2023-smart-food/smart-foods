import styles from './Card2.module.css';
import Image from '../Image/Image';

const Card2 = ({
    imageSearch,
    name,
    mass,
    price,
    website,
    buttonHandler,
    noAdd,
}) => {
    return (
        <div className={styles.container}>
            <div className={styles.image}>
                <Image queryParam={imageSearch} />
            </div>
            <div className={styles.name_block}>
                <p className={styles.name}>{name}</p>
                <p className={styles.mass}>{mass} g</p>
            </div>
            <div className={styles.choices}>
                <p className={styles.price}>${price}</p>
                <a className={styles.website} href={website} target="__blank">
                    {website.includes('amazon')
                        ? 'www.amazon.ca'
                        : 'www.saveonfoods.ca'}
                </a>
            </div>
            {noAdd ? (
                false
            ) : (
                <div className={styles.addItem}>
                    <button
                        onClick={() => {
                            buttonHandler({
                                imageSearch,
                                name,
                                mass,
                                price,
                                website,
                            });
                        }}
                    >
                        Add
                    </button>
                </div>
            )}
        </div>
    );
};

export default Card2;
