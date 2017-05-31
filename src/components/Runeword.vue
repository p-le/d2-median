<template>
  <div class="hello">
      <p class="white--text">{{ choices }}</p>
      <v-checkbox label="John" v-model="choices" value="John" light></v-checkbox>
      <v-checkbox label="Jacob" v-model="choices" value="Jacob" light></v-checkbox>
  </div>
</template>

<script>
export default {
  name: 'runeword',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      choices: []
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
