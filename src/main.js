import Vue from 'vue'
import axios from 'axios';
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// import ElementPlus from 'element-plus';
// import 'element-plus/lib/theme-chalk/index.css'
import store from './store'




axios.defaults.baseURL = 'you is host';
Vue.prototype.$axios = axios;

Vue.use(ElementUI)

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
})