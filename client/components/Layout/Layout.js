import styles from "./Layout.module.css";

const Layout = ({ children }) => {
	return (
		<div className={styles.container}>
			<header className={styles.header}>SmartFoods</header>
			<main>{children}</main>
		</div>
	);
};

export default Layout;
