import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { CartProvider } from './components/CartProvider';
import { ChakraProvider } from '@chakra-ui/react';
import theme from './utils/Theme';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <CartProvider>
      <ChakraProvider>
        <App />
      </ChakraProvider>
    </CartProvider>
  </React.StrictMode>
);
reportWebVitals();