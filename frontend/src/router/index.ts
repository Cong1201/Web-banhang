import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Home from '@/pages/Home/index.vue'

Vue.use(VueRouter)
const routes: Array<RouteConfig> = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/products',
    component: () => import('../pages/Products/index.vue')
  },
  {
    path: '/product_detail',
    component: () => import('../pages/Products/detail.vue')
  },
  {
    path: '/Admin',
    component: () => import('@/pages/Admin/index.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
