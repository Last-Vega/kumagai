<template>
  <v-app>
    <v-main>
      <router-view />
      <Navigation />
    </v-main>
  </v-app>
</template>

<script>
import Navigation from '@/components/Navigation'
export default {
  name: 'App',
  components: {
    Navigation
  },
  data () {
    return {
    }
  },
  methods: {}
}
</script>
