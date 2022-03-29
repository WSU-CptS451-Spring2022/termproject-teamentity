<template>
  <div class="container">
      <!-- "Welcome" page header -->
      <div style="padding-bottom:25px; padding-top:25px">
        <h1>Welcome to Yelp Database</h1>
      </div>
      <center>
        <b-button-toolbar style="padding-top:25px;padding-left:350px;padding-right:350px">
          <!-- Select State-->
          <b-button-group>
            <b-button variant="outline-dark"><b-icon icon="ui-checks" font-scale="5" v-on:click="onClickManageStates"></b-icon> <br> <strong>&nbsp;&nbsp;&nbsp; Retrieve&nbsp;&nbsp;&nbsp;<br> States</strong></b-button>  
          </b-button-group>
        </b-button-toolbar>
      </center>
  </div>
</template>

<script>


export default {
    name: 'Homepage',
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
        onClickManageStates() {
            this.$router.push({ path: '/testpackages' });
        },
    }
}


</script>