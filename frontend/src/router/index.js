import Vue from 'vue'
import VueRouter from 'vue-router'
import LatentSpace from '../views/LatentSpace.vue'
// import Login from '../views/Login.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/ito',
    name: 'Ito',
    component: LatentSpace
  },
  {
    path: '/mori',
    name: 'Mori',
    component: LatentSpace
  },
  {
    path: '/matsu',
    name: 'Matsu',
    component: LatentSpace
  },
  {
    path: '/tutorial',
    name: 'tutorial',
    component: LatentSpace
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
