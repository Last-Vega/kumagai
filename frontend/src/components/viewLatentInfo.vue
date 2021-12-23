<template>
<v-app>
  <highcharts :options="options" ref="chart"></highcharts>
  <v-container class="grey lighten-5">
    <v-row no-gutters>
        <v-col cols="12" sm="5">
          <v-simple-table>
            <template v-slot:default>
              <caption>
                ホバーした企業
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
                ホバーした単語
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
  </v-app>
</template>

<script>

export default {
  name: 'DisplayLatentSpace',
  props: {
    options: {
      type: Object,
      required: true
    },
    companyItems: {
      type: Object,
      required: true
    },
    termItems: {
      type: Object,
      required: true
    }
  },
  components: {
  },
  data () {
    return {

    }
  },
  methods: {

  }

}
</script>
