<template>
<div>
  <v-form>
    <v-row no-gutters>
      <v-col col="6">
        <v-text-field v-model="query" placeholder="企業名は正式名称で入力してください" label="例)株式会社熊谷組" class="queryFileds"></v-text-field>
      </v-col>
      <v-col col="6">
        <v-btn v-on:click="submit">
          検索する
        </v-btn>
      </v-col>
    </v-row>
  </v-form>
  <div v-if="showFlag===true">
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
            <td>{{queryX}}</td>
            <td>{{queryY}}</td>
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
          <tr
            v-for="(company, index) in closeCompany"
            :key="index"
            >
            <td>{{company}}</td>
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
          <tr
            v-for="(term, index) in closeTerm"
            :key="index"
            >
            <td>{{term}}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
  <div v-else>
    <p>ヒットしませんでした</p>
  </div>
</div>
</template>

<script>
import companyInfo from '@/assets/latentC1223.json'
import termInfo from '@/assets/latentT1223.json'

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
      query: '',
      closeCompany: [],
      closeTerm: [],
      showFlag: false,
      companyInfo: '',
      termInfo: '',
      queryX: '',
      queryY: ''
    }
  },
  methods: {
    submit () {
      this.closeCompany = []
      this.closeTerm = []
      let filterIndex = -1
      let flag = -1
      if (this.companyName.includes(this.query)) {
        filterIndex = this.companyName.indexOf(this.query)
        flag = 0
      } else if (this.termName.includes(this.query)) {
        filterIndex = this.termName.indexOf(this.query)
        flag = 1
      } else {
        filterIndex = -1
        flag = -1
        this.showFlag = false
      }
      if (filterIndex !== -1) {
        this.showFlag = true
        if (flag === 0) {
          this.queryX = this.companyInfo[filterIndex].x
          this.queryY = this.companyInfo[filterIndex].y
          this.calcCompanyDistance(filterIndex, this.companyInfo[filterIndex].x, this.companyInfo[filterIndex].y, false)
          this.calcTermDistance(filterIndex, this.companyInfo[filterIndex].x, this.companyInfo[filterIndex].y, true)
        } else if (flag === 1) {
          this.queryX = this.termInfo[filterIndex].x
          this.queryY = this.termInfo[filterIndex].y
          this.calcCompanyDistance(filterIndex, this.termInfo[filterIndex].x, this.termInfo[filterIndex].y, true)
          this.calcTermDistance(filterIndex, this.companyInfo[filterIndex].x, this.companyInfo[filterIndex].y, false)
        }
      }
    },
    calcCompanyDistance (index, x, y, flag) {
      const distanceList = []
      this.companyInfo.forEach((value) => {
        const tempObj = {}
        const distance = Math.sqrt((value.x - x) ** 2 + (value.y - y) ** 2)
        tempObj.key = value.company
        tempObj.value = distance
        distanceList.push(tempObj)
      })
      distanceList.sort((a, b) => a.value - b.value)
      if (flag === true) {
        for (let i = 0; i < 5; i++) {
          this.closeCompany.push(distanceList[i].key)
        }
      } else {
        for (let i = 1; i < 6; i++) {
          this.closeCompany.push(distanceList[i].key)
        }
      }
    },
    calcTermDistance (index, x, y, flag) {
      const distanceList = []
      this.termInfo.forEach((value) => {
        const tempObj = {}
        const distance = Math.sqrt((value.x - x) ** 2 + (value.y - y) ** 2)
        tempObj.key = value.term
        tempObj.value = distance
        distanceList.push(tempObj)
      })
      distanceList.sort((a, b) => a.value - b.value)
      if (flag === true) {
        for (let i = 0; i < 5; i++) {
          this.closeTerm.push(distanceList[i].key)
        }
      } else {
        for (let i = 1; i < 6; i++) {
          this.closeTerm.push(distanceList[i].key)
        }
      }
    }
  },
  created () {
    this.companyInfo = companyInfo.key
    this.termInfo = termInfo.key
  }
}
</script>

<style scoped>
/* .queryFileds{
  width: 50%;
} */
</style>
