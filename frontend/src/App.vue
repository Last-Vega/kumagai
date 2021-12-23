<template>
  <v-app>
    <Navigation />
    <v-main>
    </v-main>
  </v-app>
</template>

<script>
import Navigation from '@/components/Navigation'
// import LatentSpace from '@/views/LatentSpace'
export default {
  name: 'App',
  components: {
    Navigation
    // LatentSpace
  },
  data () {
    return {
    }
  },
  methods: {}
}
</script>
