<template>
  <!-- can change class to "container-fluid" to get full width of browser window. -->
  <div id="app" class="container">
    <!-- Render the header on every page -->
    <SiteHeader/>

    <!-- Render the router view based on the current url -->
    <router-view></router-view>
  </div>
</template>

<script>

import VueRouter from 'vue-router';
import SiteHeader from './components/SiteHeader.vue';
import Homepage from './components/Homepage.vue';
import ViewBusinesses from './components/ViewBusinesses.vue';
import Display from './components/display.vue';


// Router to determine which component gets loaded based on the current url
const router = new VueRouter({
  base: __dirname,
  routes: [
    { path: '/', component: Homepage },
    { path: '/testpackages', component: ViewBusinesses },
    { path: '/display', component: Display },
  ],
});

export default {
  router,
  name: 'App',
  components: {
    SiteHeader,
  }
};
</script>

<style>
</style>
