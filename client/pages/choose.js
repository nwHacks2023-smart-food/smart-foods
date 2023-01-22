import Layout from "../components/Layout/Layout.js";
import styles from "../styles/choose.module.css";
import Button from "../components/Button/Button";
import Card from "../components/Card/Card";

const Choose = () => {
	return (
		<Layout>
			<div className={styles.container}>
				<h2 className={styles.step}>Step 1: Choose your foods</h2>
				<div className={styles.content}>
					<div className={styles.input}>
						<input type="text" placeholder="Enter a food:" />
						<button className={styles.addButton}>+</button>
					</div>
					<div className={styles.cards}>
						<Card
							imageSearch="m"
							name="Orange"
							mass="50g"
							calories="200"
							sugar="14g"
							protein="2g"
						/>
					</div>
				</div>
				<Button text="Next" path="/choose" />
			</div>
		</Layout>
	);
};

export default Choose;
