import Vue from 'vue'
import Router from 'vue-router'
import Runeword from '@/components/Runeword'
import NotFound from '@/components/NotFound'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Runeword',
      component: Runeword
    },
    { path: '*', component: NotFound }
  ]
})
