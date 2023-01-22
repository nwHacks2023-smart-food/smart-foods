import Layout from "../components/Layout/Layout.js";
import styles from "../styles/choose.module.css";
import Button from "../components/Button/Button";

const Choose = () => {
	return (
		<Layout>
			<div className={styles.container}>
				<h2 className={styles.step}>Step 1: Choose your foods</h2>
				<div className={styles.card}>
					<input type="text" placeholder="Enter a food:" />
				</div>
				<Button text="Next" path="/choose" />
			</div>
		</Layout>
	);
};

export default Choose;
