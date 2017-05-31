<template>
  <div>
    <v-layout row wrap>
      <v-flex xs4>
        <v-card>
          <v-card-text class="level">
            <div class="level_group">
              <div class="level_slider">
                <v-slider v-model="minLevel" dark thumb-label step="1" max=125 min=0></v-slider>
              </div>
              <div class="level_number">
                <v-text-field label="Min Level" dark v-model="minLevel" type="number"></v-text-field>
              </div>
            </div>
            <div class="level_group">
              <div class="level_slider">
                <v-slider v-model="maxLevel" dark thumb-label step="1" max=125 min=0></v-slider>
              </div>
              <div class="level_number">
                <v-text-field label="Max Level" dark v-model="maxLevel" type="number"></v-text-field>
              </div>
            </div>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs12>
        <v-card>
          <v-card-text class="rw_types">
            <div class="rw_type" v-for="rwType of rwTypes">
              <v-checkbox  :label="rwType" v-model="searchTypes" :value="rwType" dark primary hide-details></v-checkbox>
            </div>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <div class="search">
      <v-btn floating large primary @click.native="search">
        <v-icon light>search</v-icon>
      </v-btn>
    </div>
    <div v-if="rwResult.length > 0" class="result">
      <v-data-table
        :headers="headers"
        :items="rwResult"
        hide-actions
        class="elevation-1"
      >
        <template slot="items" scope="props">
          <td class="text-xs">{{ props.item.name }}</td>
          <td class="text-xs">{{ props.item.level }}</td>
          <td class="text-xs" v-html="props.item.runes"></td>
          <td class="text-xs">{{ props.item.rwType }}</td>
          <td class="text-xs" v-html="props.item.description"></td>
        </template>
      </v-data-table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'runeword',
  props: [
    'rws'
  ],
  data () {
    return {
      minLevel: 0,
      maxLevel: 125,
      rwTypes: [],
      searchTypes: [],
      rwResult: [],
      headers: [
        { text: 'Name', value: 'name', left: true },
        { text: 'Level', value: 'level', left: true },
        { text: 'Runes', value: 'name', left: true },
        { text: 'Type', value: 'rwType', left: true },
        { text: 'Description', value: 'description', left: true }
      ]
    }
  },
  methods: {
    search () {
      this.rwResult = this.rws.filter(rw => {
        let isOk = false
        if (rw.level >= this.minLevel && rw.level <= this.maxLevel) {
          if (this.searchTypes.includes(rw.rwType)) {
            isOk = true
          }
        }
        return isOk
      })
      this.rwResult = this.rwResult.map(rw => {
        rw.description = rw.description.join('<br />')
        const runes = rw.runes
        const tmp = []
        for (let i = 0; i < runes.length; i++) {
          if (!runes[i].includes('Rune')) {
            tmp.push(`${runes[i]} ${runes[i + 1]}`)
            i++
          } else {
            tmp.push(runes[i])
          }
        }
        rw.runes = tmp.join('<br />')
        return rw
      })
    }
  },
  created: function () {
    const set = new Set(this.rws.map(rw => rw.rwType))
    this.rwTypes = [...set]
  }
}
</script>

<style scoped>
.level_group {
  display: flex;
}

.level_group .level_slider {
  width: 70%;
  display: flex;
  align-items: center;
}
.level_group .level_number {
  width: 30%;
  padding-left: 20px;
  display: flex;
  align-items: center;
}

.input-group--slider.input-group--dark label {
  font-size: 14px;
}
.rw_types {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.rw_type {
  min-width: 270px;
  display: inline-block;
}
.search {
  display: flex;
  justify-content: center;
}
.result {
  padding-bottom: 30px;
}
</style>
