import styles from "./Card.module.css";
import Image from "../Image/Image";

const Card = ({ imageSearch, name, mass, calories, sugar, protein }) => {
	return (
		<div className={styles.container}>
			<div className={styles.image}>
				<Image queryParam={imageSearch} />
			</div>
			<div className={styles.name_block}>
				<p className={styles.name}>{name}</p>
				<p className={styles.mass}>{mass} g</p>
			</div>
			<div className={styles.nutrients}>
				<p>Calories: {calories}</p>
				<p>Sugar: {sugar} g</p>
				<p>Protein: {protein} g</p>
			</div>
		</div>
	);
};

export default Card;
