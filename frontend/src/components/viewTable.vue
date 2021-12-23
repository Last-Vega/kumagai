<template>
<div>
  <v-form>
    <v-row no-gutters>
      <v-col col="6">
        <v-text-field v-model="query" class="queryFileds"></v-text-field>
      </v-col>
      <v-col col="6">
        <v-btn v-on:click="submit">
          検索する
        </v-btn>
      </v-col>
    </v-row>
  </v-form>
  <v-simple-table>
    <template v-slot:default>
      <caption>
        検索された単語の座標
      </caption>
      <thead>
        <tr>
          <th class="text-left">X</th>
          <th class="text-left">Y</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>000</td>
          <td>111</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
  <v-simple-table>
    <template v-slot:default>
      <caption>
        近くの企業
      </caption>
      <thead>
        <tr>
          <th class="text-left">Company</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td></td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
  <v-simple-table>
    <template v-slot:default>
      <caption>
        近くの単語
      </caption>
      <thead>
        <tr>
          <th class="text-left">Term</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td></td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</div>
</template>

<script>
export default {
  name: 'ViewTabel',
  props: {
    companyName: {
      type: Array,
      required: true
    },
    termName: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
      query: ''
    }
  },
  methods: {
    submit () {
      let filterIndex = -1
      if (this.companyName.includes(this.query)) {
        filterIndex = this.companyName.indexOf(this.query)
      } else if (this.termName.includes(this.query)) {
        filterIndex = this.termName.indexOf(this.query)
      } else {
        filterIndex = -1
      }
      console.log(filterIndex)
    }
  }

}
</script>

<style scoped>
/* .queryFileds{
  width: 50%;
} */
</style>
