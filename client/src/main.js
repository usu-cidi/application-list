import { createApp } from 'vue'
import {createRouter, createWebHistory} from 'vue-router'

import HomePageComponent from './components/HomePage.vue'
import BugReportComponent from './components/BugReport.vue'
import SubmittedComponent from './components/SubmittedPage.vue'

import App from './App.vue'

const router = createRouter({
    history: createWebHistory(),
    routes:[
        { path: '/', component: HomePageComponent},
        { path: '/bug-report', component: BugReportComponent},
        { path: '/submitted', component: SubmittedComponent},
    ]
});

const app = createApp(App)
app.use(router)
app.mount('#app')
