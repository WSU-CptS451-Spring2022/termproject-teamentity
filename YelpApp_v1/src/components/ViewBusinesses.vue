<template>
  <div class="container">
    <!-- View Businesses Page Header-->
    <div style="padding-bottom:50px; padding-top:25px">
        <h1>View Businesses</h1>
    </div>
    <div style="padding-bottom:25px">
        <b-row>
            <b-col>
                <!-- Search bar -->
                <b-input-group>
                    <!-- Activates search method when input in search bar changes -->
                    <b-form-input placeholder="Search..." @input="searchBusiness()" v-model="curSearch"></b-form-input>
                    <b-input-group-append>
                        <!-- search button, mostly aesthetic, but also activates search method when clicked -->
                        <b-button variant="outline-secondary" @click="searchBusiness()">
                            <b-icon icon="search"></b-icon>
                        </b-button>
                    </b-input-group-append>
                </b-input-group>
            </b-col>
            <b-col>
                <!-- Enroll new Client button, will redirect user to New Client page in the future -->
                <b-button variant="success" title="Note" @click="redirectToCreateTestPackage()">
                    <b-icon icon="plus-circle"></b-icon>
                    Retrieve States
                </b-button>
            </b-col>
        </b-row>
    </div>
    <div>
        <!-- Client table, renders the filteredClients (Clients that meet current search criteria) -->
        <md-table v-model="filteredTestPackages" style="padding-bottom:50px">
            <md-table-row slot="md-table-row" slot-scope="{ item }">
                <md-table-cell md-label="Name" md-sort-by="name"><router-link :to="`/testpackages/${item.testPackageId}`" class="nav-link">{{ item.packageName }}</router-link></md-table-cell>
                <md-table-cell md-label="Number of Tests" md-sort-by="numTests">{{ item.testSettings.length }}</md-table-cell>
            </md-table-row>
        </md-table>
    </div>
  </div>
</template>

<script>
import { MdTable } from 'vue-material/dist/components';
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import Vue from 'vue';
Vue.use(MdTable);

export default {
    name: 'ManageTestPackages',
    components: {
    },
    data() {
        return {
            curSearch: "",
        }
    },
    computed: {
        filteredTestPackages() {
            return this.searchBusiness();
        }
    },
    mounted () {
      var internal = this;

      // when the component mounts, query which Test Packages are associated with the Customer (user).
      this.$store.dispatch('getTestPackages');

    },
    props: {
        searchVal: String
    },
    methods: {
        searchBusiness() {
            var internal = this;

            // if there aren't any Test Packages, return an empty array
            if (this.$store.state.testPackages == null || this.$store.state.testPackages.length == 0) {
                return [];
            }

            // make search lowercase so that it isn't case sensitive
            const searchString = internal.curSearch.toLowerCase();

            // If any part of the Client's name, email, or phone number match the search string, show them as a search result
            const results = this.$store.state.testPackages.filter( function(test) {
                if (test.packageName.toLowerCase().includes(searchString)) {
                    return test;
                }
            });
            return results;
        },

        redirectToCreateTestPackage() {
            this.$router.push({ path: '/display' });
        },
    }
}


</script>

<style>
</style>
