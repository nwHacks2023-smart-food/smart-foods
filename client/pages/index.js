import styles from "../styles/index.module.css";

export default function Home() {
	return (
		<div className={styles.container}>
			<div className={styles.banner}>
				<h1>SmartFoods</h1>
				<p>Create your smart grocery list now!</p>
			</div>
			<button>Get Started</button>
		</div>
	);
}
