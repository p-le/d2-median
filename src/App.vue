<template>
  <v-app>
    <v-toolbar>
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <main>
      <v-container fluid>
        <v-slide-y-transition mode="out-in">
          <router-view></router-view>
        </v-slide-y-transition>
      </v-container>
    </main>
    <v-footer fixed>
      <span>&copy; 2017 - phu.le.dev@gmail.com</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    data () {
      return {
        title: 'Median XL Runewords'
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
