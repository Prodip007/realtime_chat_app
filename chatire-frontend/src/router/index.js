import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Chat from '@/components/Chat'
import UserAuth from '@/components/UserAuth'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/chats',
    name: 'Chat',
    component: Chat
  },
  {
    path: '/auth',
    name: 'UserAuth',
    component: UserAuth
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if(localStorage.getItem('authToken') != null || to.path == '/auth'){
    next()
  } else {
    next('/auth')
  }
})

export default router
