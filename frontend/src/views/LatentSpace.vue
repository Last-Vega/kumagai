<template>
  <v-app>
    <v-row no-gutters>
      <v-col cols="12" sm="9">
        <ViewLatentSpace :options="options" :companyItems="companyItems" :termItems="termItems" />
      </v-col>
      <!-- <v-col cols="12" sm="1"> </v-col> -->
      <v-col cols="12" sm="3">
        <ViewTabel :companyName="companyName" :termName="termName" />
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
import {
  companyTableData,
  termTableData,
  chartOptions
} from '@/components/createLatentSpace'
import companyInfo from '@/assets/latentC.json'
import termInfo from '@/assets/latentT.json'
import ViewTabel from '@/components/viewTable'
import ViewLatentSpace from '@/components/viewLatentInfo'
export default {
  name: 'LatentSpace',
  components: {
    ViewTabel,
    ViewLatentSpace
  },
  data () {
    return {
      options: chartOptions,
      headers: [
        { text: 'Title', value: 'title' },
        { text: 'Authors', value: 'author' },
        { text: 'Conference', value: 'conference' },
        { text: 'Year', value: 'year' }
      ],
      companyItems: companyTableData,
      termItems: termTableData,
      companyName: [],
      companyXY: [],
      termName: [],
      termXY: [],
      query: ''
    }
  },
  methods: {},
  created () {
    const companyData = companyInfo.key
    const termData = termInfo.key
    for (let i = 0; i < companyData.length; i++) {
      this.companyName.push(companyData[i].company)
      this.companyXY.push([companyData[i].x, companyData[i].y])
    }
    for (let i = 0; i < termData.length; i++) {
      this.termName.push(termData[i].term)
      this.termXY.push([termData[i].x, termData[i].y])
    }
    this.options.series[0].dataLabal = this.companyName
    this.options.series[0].data = this.companyXY
    this.options.series[1].dataLabal = this.termName
    this.options.series[1].data = this.termXY
  }
}
</script>
