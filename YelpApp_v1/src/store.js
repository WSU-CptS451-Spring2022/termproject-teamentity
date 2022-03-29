import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const adminApiString = "http://localhost:7992/v1/api/admin";
const networkApiString = "http://localhost:7982/v1/api";
// 320227ee-381b-40d0-a14a-e21775fb3c91

// Store for our application's state.
export default new Vuex.Store({
  state: {
    account: null,
    clients: [],
    testPackages: [],
    clientTestPackageEnrollment: [],
    clientTestResults: [],
  },
  mutations: {
    setClients(state, clients) {
      state.clients = clients;
    },
    setAccount(state, customer){
      state.account = customer;
    },
    setTestPackages(state, testPackages) {
      state.testPackages = testPackages;
    },
    setClientTestPackageEnrollment(state, clientTestPackageEnrollment) {
      state.clientTestPackageEnrollment = clientTestPackageEnrollment;
    },
    setClientTestResults(state, clientTestResults) {
      state.clientTestResults = clientTestResults;
    },
  },
  actions: {
      getClients({ commit }) {
        
        // do not attempt to get Clients if not logged in.
        if (this.state.account == null) {
          return;
        }

        // get the Clients from the Admin API and set the state for Clients
        const apiUri = adminApiString + "/clients/" + this.state.account;
        return new Promise((resolve, reject) => {
          axios.get(apiUri).then((results) => { 
            commit('setClients', results.data.clients);
            resolve(results);
          }).catch((error) => {
            reject(error);
          });
        });
      },
      getTestPackages ({ commit }) {
        
        // do not attempt to get Test Packages if not logged in.
        if (this.state.account == null) {
          return;
        }
        
        // get the Test Packages from the Admin API and set the state for Test Packages
        // TODO: Make this no longer hard-coded once login is set-up.
        const apiUri = adminApiString + "/" + this.state.account + "/configs/tests";
        return new Promise((resolve, reject) => {
          axios.get(apiUri).then((results) => { 
            commit('setTestPackages', results.data.tests); 
            resolve(results);
          }).catch((error) => {
            reject(error);
          });
        });
      },
      getClientTestPackageEnrollments( commit, { clientId }) {

        // build the uri for the request
        const apiUri = adminApiString + "/clients/" + clientId + "/tests";

        // get the Test Packages that the Client is enrolled in
        return new Promise((resolve, reject) => {
          fetch(apiUri, {
            method: "GET",
          }).then((results) => {
            results.json().then((responseJson) => {
              console.log(responseJson);
              this.commit('setClientTestPackageEnrollment', responseJson.tests); 
              resolve(results);
            }).catch((error) => {
              reject(error);
            });
          }).catch((error) => {
            reject(error);
          });
        });
      },
      getClientTestResults( commit, { clientId }) {
        
        // build the uri for the request
        const apiUri = networkApiString + "/clients/" + clientId + "/results";

        // get the test results for the Client
        return new Promise((resolve, reject) => {
          fetch(apiUri, {
            method: "GET",
          }).then((results) => {
            results.json().then((responseJson) => {
              console.log(responseJson);
              this.commit('setClientTestResults', responseJson.results); 
              resolve(results);
            }).catch((error) => {
              reject(error);
            });
          }).catch((error) => {
            reject(error);
          });
        });
      },
      postClient( commit, {name, phoneNumber, email, testPackagesToEnroll }) {

          // do not attempt to post a Client if not logged in.
          if (this.state.account == null) {
            return;
          }

          const data = {name, phoneNumber, email};
          let apiResponseStatus;
          const apiClientsUri = adminApiString + "/clients";

          // POST new Client to the API
          return new Promise((resolve, reject) => {
            fetch(apiClientsUri, {
            method: "POST",
            body: JSON.stringify(data),
            }).then((response) => {
              apiResponseStatus = response.status;
              
              // convert response into JSON
              response.json().then((responseJson) => {
                console.log(responseJson);
                let successCount = 0;
                const customerId = this.state.account;
                const clientId = responseJson.omitempty.id;
                console.log("ClientId", clientId);

                // associate the Client with a specific Customer
                const clientIds = []
                clientIds.push(clientId);
                const managesPost = {customerId, clientIds};
                const managesUri = adminApiString + "/clients/manages";

                console.log(JSON.stringify(managesPost));

                fetch(managesUri, {
                  method: "POST",
                  body: JSON.stringify(managesPost),
                }).then((managesResponse) => {
                  // success
                }).catch((error) => {
                  console.log("ERROR:", error);
                  reject(error); // failure
                });

                // for each test package enrollment, send a POST request
                for(let i = 0; i < testPackagesToEnroll.length; i++) {
                  let testPackageId = testPackagesToEnroll[i].testPackageId;
                  const testPackageEnrollmentPost = {clientId, customerId, testPackageId}
                  const apiTestPackageEnrollmentUri = adminApiString + "/clients/enrollment";
                  
                  fetch(apiTestPackageEnrollmentUri, {
                    method: "POST",
                    body: JSON.stringify(testPackageEnrollmentPost),
                  }).then((testPackageResponse) => {
                    successCount += 1;
                  });
                }
                resolve(apiResponseStatus); 
              });              
            }).catch((error) => {
              console.error('ERROR:', error); 
              reject(error);
            });
          });
      },
      postClientTestPackageEnrollments( commit, { testPackagesToEnroll, clientId }) {
        
        // do not attempt to enroll Clients in Test Packages if not logged in
        if (this.state.account == null) {
          return;
        }
        
        const customerId = this.state.account;
        const apiUri = adminApiString + "/clients/enrollment";
        let successCount = 0;

        return new Promise((resolve, reject) => {
          for(let i = 0; i < testPackagesToEnroll.length; i++) {
            let testPackageId = testPackagesToEnroll[i].testPackageId;
            const testPackageEnrollmentPost = {clientId, customerId, testPackageId}
            
            fetch(apiUri, {
              method: "POST",
              body: JSON.stringify(testPackageEnrollmentPost),
            }).then((testPackageResponse) => {
              successCount += 1;
              if (successCount == testPackagesToEnroll.length) {
                resolve(testPackageResponse.status);
              }
            }).catch((error) => {
              reject(error);
            });
          }
        });
      },
      postCustomer( commit, {name, username, email, password}) {
        const data = {name, username, email, password};
        const apiUri = adminApiString + "/register";

        return new Promise((resolve, reject) => {
          fetch(apiUri, {
          method: "POST",
          body: JSON.stringify(data),
          }).then((response) => { 
            console.log("response from API:", response); 
            console.log("response status:", response.status);            
            resolve(response.status); 
          }).catch((error) => {
            console.error('ERROR:', error); 
            reject(error);
          });
        });
      },
      postTestPackage( commit, { packageName, testSettings }) {
        
        // do not attempt to create a Test Package if not logged in.
        if (this.state.account == null) {
          return;
        }

        const customerID = this.state.account;
        const data = { customerID, packageName, testSettings };
        const apiUri = adminApiString + "/configs/tests";

        return new Promise((resolve, reject) => {
          fetch(apiUri, {
          method: "POST",
          body: JSON.stringify(data),
          }).then((response) => { 

            resolve(response.status); 
          }).catch((error) => {
            console.error('ERROR:', error); 
            reject(error);
          });
        });
      },
      getCustomer(commit, {email, password}) {
        const data = {email, password};
        const apiUri = adminApiString + "/login";
        return new Promise((resolve, reject) => {
          fetch(apiUri, {
          method: "POST",
          body: JSON.stringify(data),
          }).then((response) => { 
            response.json().then((responseJson) => {
              console.log("response from API:", responseJson); 
              console.log("response status:", response.status);
              if (responseJson && responseJson.customer && responseJson.customer.id) {
                this.commit('setAccount', responseJson.customer.id);
                resolve(response.status); 
              } else {
                reject(response.status);
              }
            });
          }).catch((error) => {
            console.error('ERROR:', error); 
            reject(error);
          });
        });
      },
      logOut({commit}){
        commit('setAccount', null);
        commit('setClients', []);
        commit('setTestPackages', []);
      }
   }
});