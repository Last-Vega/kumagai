<template>
<div>
    <section class="charts">
      <highcharts :options="options" ref="chart"></highcharts>
    </section>
  <v-container class="grey lighten-5">
    <v-row no-gutters>
        <v-col cols="12" sm="5">
          <v-simple-table>
            <template v-slot:default>
              <caption>
                マウスがホバーした企業
              </caption>
              <thead>
                <tr>
                  <th class="text-left">Company</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{{ companyItems.company }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-col>
        <v-col cols="12" sm="2"> </v-col>
        <v-col cols="12" sm="5">
          <v-simple-table>
            <template v-slot:default>
              <caption>
                マウスがホバーした単語
              </caption>
              <thead>
                <tr>
                  <th class="text-left">Term</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{{ termItems.term }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-col>
    </v-row>
    </v-container>
  </div>
</template>

<script>
import {
  companyTableData,
  termTableData,
  chartOptions
} from '@/components/createLatentSpace'
import companyInfo from '@/assets/latentC.json'
import termInfo from '@/assets/latentT.json'
export default {
  name: 'DisplayLatentSpace',
  components: {
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
      termXY: []

    }
  },
  methods: {

  },
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
