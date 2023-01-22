import { ItemsProvider } from '../context/items-context';
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
    return (
        <ItemsProvider>
            <Component {...pageProps} />
        </ItemsProvider>
    );
}

export default MyApp;
