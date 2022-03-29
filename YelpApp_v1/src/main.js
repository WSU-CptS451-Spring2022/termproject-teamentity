import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import { MdTable, MdCheckbox, MdRipple, MdContent } from 'vue-material/dist/components'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import VueRouter from 'vue-router';
import VeeValidate from 'vee-validate';

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueRouter);
Vue.use(MdTable);
Vue.use(MdCheckbox);
Vue.use(MdRipple);
Vue.use(MdContent);


Vue.config.productionTip = false;

import store from './store';

new Vue({
  render: (h) => h(App),
  store,
}).$mount('#app');
