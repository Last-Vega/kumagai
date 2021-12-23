<template>
  <v-app>
    <v-navigation-drawer app v-model="drawer" clipped>
      <v-container>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title grey--text text--darken-2">
              Menu
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list dense nav>
          <v-list-item v-for="nav_list in nav_lists" :key="nav_list.name" :to="nav_list.link">
            <v-list-item-icon>
              <v-icon>{{ nav_list.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ nav_list.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-container>
    </v-navigation-drawer>
    <v-app-bar color="primary" dark app clipped-left>
    <v-app-bar-nav-icon @click="drawer=!drawer">

      </v-app-bar-nav-icon>
        <v-toolbar-title>
          特許データ分析
        </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>

    <v-footer color="primary" dark app>
    </v-footer>
  </v-app>

</template>

<script>
// import displayLatentInfo from '@/components/displayLatentInfo'
export default {
  components: {
    // displayLatentInfo
  },
  data () {
    return {
      drawer: false,
      nav_lists: [
        { name: 'Home', icon: 'mdi-home', link: '/' }
      ]
    }
  }
}
</script>
