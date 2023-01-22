import styles from "./Card2.module.css";
import Image from "../Image/Image";

const Card2 = ({name, mass, priceObject}) => {
	return (
		<div className={styles.container}>
			<div className={styles.image}>
				<Image queryParam={imageSearch} />
			</div>
			<div className={styles.name_block}>
				<p className={styles.name}>{name}</p>
				<p className={styles.mass}>{mass}</p>
			</div>
			<div className={styles.nutrients}>
				<p>Calories: {calories}</p>
				<p>Sugar: {sugar}</p>
				<p>Protein: {protein}</p>
			</div>
		</div>
	);
};

export default Card2;
