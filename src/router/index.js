import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
import Finance from '@/views/Finance.vue';
import Admin from '../components/Admin.vue'
import Commodity from '../components/Commodity.vue';
import Index from '../components/Index.vue'
import Attendance from '../components/Attendance.vue'
import Purchasing from '../components/Purchasing.vue';
import Department from '../components/Department.vue';

Vue.use(VueRouter)

const isAuthenticated = () => {
    return !!sessionStorage.getItem('user_id');
};

const routes = [{
        path: '/auth/finance',
        name: 'finance',
        component: Finance
    },
    {
        path: '/about',
        name: 'about',
        component: () =>
            import ('../views/AboutView.vue')
    },
    {
        path: '/auth/login',
        component: Login,
        beforeEnter: (to, from, next) => {
            if (isAuthenticated()) {
                next('/');
            } else {
                next();
            }
        }
    },
    {
        path: '/auth/register',
        component: Register,
        beforeEnter: (to, from, next) => {
            if (isAuthenticated()) {
                next('/');
            } else {
                next();
            }
        }
    },
    {
        path: '/auth/admin',
        component: Admin,
    },
    {
        path: '/auth/Department',
        component: Department,
    },
    {
        path: '',
        component: Index
    },
    {
        path: '/auth/Commodity',
        component: Commodity,
    },
    {
        path: '/auth/Purchasing',
        component: Purchasing,
    },
    {
        path: '/auth/Attendance',
        component: Attendance
    }
]

const router = new VueRouter({
    routes,
    mode: 'history'
})

export default router