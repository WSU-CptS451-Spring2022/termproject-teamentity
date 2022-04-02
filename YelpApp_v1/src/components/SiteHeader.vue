<template>
  <b-navbar type="dark" variant="dark">
    <b-navbar-nav>
       <!-- Yelp logo -->
      <b-navbar-brand style="padding-left:25px">
      <img src="../assets/yelp.png" class="d-inline-block align-top" alt="Yelp" width="32" height="32">
        YELP
        </b-navbar-brand>
   
      
      <!-- Link to Homepage -->
      <b-nav-item><b-icon icon="house" style="padding-right:2px"></b-icon><router-link to="/" style="color:darkgray">Home</router-link></b-nav-item>

      <!-- Link to Show Business Page -->
      <b-nav-item><router-link to="/display" style="color:darkgray">Catagories</router-link></b-nav-item>

    </b-navbar-nav>
    
    <!-- Dropdown for Account -->
    <b-navbar-nav>
      <b-nav-item-dropdown text="Account" right>
          <b-dropdown-item href="#">Settings</b-dropdown-item>
      </b-nav-item-dropdown>
    </b-navbar-nav>

  </b-navbar>
</template>

<script>


export default {
    name: 'SiteHeader',
    components: {

    },
    data() {
        return {
        }
    },
    mounted () {

    },
    props: {

    },
    methods: {

    }
}


</script>