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
					<form className={styles.input} action="/" method="post">
						<input type="text" placeholder="Enter a food:" />
						<button type="submit" className={styles.addButton}>+</button>
					</form>
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
