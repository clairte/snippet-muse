import axios from 'axios';
import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'

// Create the Vue app instance
const app = createApp(App);

// Configure Axios to be used globally
app.config.globalProperties.$axios = axios;

// Mount the app
app.mount('#app');
