import Layout from "../components/Layout/Layout";
import styles from "../styles/build_cart.module.css";
import Button from "../components/Button/Button";
import Card from "../components/Card/Card";

const BuildCart = () => {
	return (
		<Layout>
			<div className={styles.container}>
				<h2 className={styles.step}>Step 2: Build your cart</h2>
				<section>
					<div className={styles.content}>
						<div className={styles.cards}>
                            <h3>Compare</h3>
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
					<div className={styles.content}>
						<div className={styles.cards}>
                            <h3>Cart</h3>
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
				</section>

				<div className={styles.buttons}>
					<Button text="Go Back" path="/choose" />
					<Button text="View Summary" path="/build_cart" />
				</div>
			</div>
		</Layout>
	);
};

export default BuildCart;
