<template>
  <v-app>
    <v-navigation-drawer
      persistent
      clipped
      v-model="drawer"
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
        >
          <v-list-tile value="true">
            <v-list-tile-action>
              <v-icon light v-html="item.icon"></v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title v-text="item.title"></v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar>
      <v-toolbar-side-icon @click.native.stop="drawer = !drawer" light></v-toolbar-side-icon>
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <main>
      <v-container fluid>
        <v-slide-y-transition mode="out-in">
          <v-layout column align-center>
            <router-view></router-view>
          </v-layout>
        </v-slide-y-transition>
      </v-container>
    </main>
    <v-footer fixed>
      <span>&copy; 2017 - phu.le.dev@gmail.com</span>
    </v-footer>
  </v-app>
</template>

<script>
  import rws from './rw.json'

  export default {
    data () {
      const menus = rws.map(rw => rw.rwType)
      return {
        drawer: true,
        items: [...new Set(menus)].map(i => {
          return {
            title: i
          }
        }),
        title: 'Median XL Runewords'
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
