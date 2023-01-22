import { useRouter } from "next/router";
import styles from "./Button.module.css";

const Button = ({ text, path }) => {
	const router = useRouter();

	return (
		<button className={styles.button} type="button" onClick={() => router.push(path)}>
			{text}
		</button>
	);
};

export default Button;
