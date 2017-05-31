import Vue from 'vue'
import Router from 'vue-router'
import Runeword from '@/components/Runeword'
import NotFound from '@/components/NotFound'

Vue.use(Router)

let basePath = '/'
if (process.env.NODE_ENV === 'production') {
  basePath = '/d2-median/'
}
export default new Router({
  mode: 'history',
  routes: [
    {
      path: basePath,
      name: 'Runeword',
      component: Runeword
    },
    { path: '*', component: NotFound }
  ]
})
