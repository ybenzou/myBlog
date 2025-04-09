import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Post from './views/Post.vue'
import Admin from './views/Admin.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/post/:id', component: Post },
  { path: '/admin', component: Admin }
]


export default createRouter({
  history: createWebHistory(),
  routes
})
