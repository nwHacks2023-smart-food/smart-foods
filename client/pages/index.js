import styles from "../styles/index.module.css";
import Button from "../components/Button/Button";

export default function Home() {
	return (
		<div className={styles.container}>
			<div className={styles.banner}>
				<h1>SmartFoods</h1>
				<p>Create your smart grocery list now!</p>
			</div>
				<Button text="Get Started" path="/choose" />
		</div>
	);
}
