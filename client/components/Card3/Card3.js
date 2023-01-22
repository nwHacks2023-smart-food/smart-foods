import styles from "./Card3.module.css";
import Image from "../Image/Image";

const Card3 = ({imageSearch, name, mass, price, website}) => {
	return (
		<div className={styles.container}>
			<div className={styles.counter}>
				<input type="number" max="10" min="1"/>
			</div>
			<div className={styles.image}>
				<Image queryParam={imageSearch} />
			</div>
			<div className={styles.name_block}>
				<p className={styles.name}>{name}</p>
				<p className={styles.mass}>{mass}</p>
			</div>
			<div className={styles.choices}>
				<p className={styles.price}>{price}</p>
				<p className={styles.website}>{website}</p>
			</div>
		</div>
	);
};

export default Card3;
