// @ts-nocheck

import { createApp } from 'vue';
import App from './App.vue';

import Buefy from '@ntohq/buefy-next';
import '@ntohq/buefy-next/dist/buefy.css';

const app = createApp(App)
app.use(Buefy);
app.mount('#app');
