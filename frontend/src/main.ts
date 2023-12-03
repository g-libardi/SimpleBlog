import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import * as VueRouter from 'vue-router'
import Feed from './pages/Feed.vue'

const routes = [
    { path: '/', component: Feed },
];

const router = VueRouter.createRouter({
    history: VueRouter.createWebHistory(),
    routes,
});

createApp(App).use(router).mount('#app');
