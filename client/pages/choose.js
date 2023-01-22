import Layout from "../components/Layout/Layout.js";
import styles from "../styles/choose.module.css";
import Button from "../components/Button/Button";
import Card from "../components/Card/Card";
import axios from "axios";


const Choose = () => {
	const test = async () => {
		const response = await axios.get('localhost:8000/api/nutrition?food=apple')
		console.log(response.data)
	}

	return (
		<Layout>
			<div className={styles.container}>
				<h2 className={styles.step}>Step 1: Choose your foods</h2>
				<div className={styles.content}>
					<div className={styles.input}>
						<input type="text" placeholder="Enter a food:" />
						<button type="submit" className={styles.addButton} onClick={test}>
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
