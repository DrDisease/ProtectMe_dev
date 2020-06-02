<template>
  <div class="wrapper">
    <side-bar>
      <template slot="links">
       
        <div>
        <base-button class="animation-on-hover" type="default" style="display:block;margin:auto;  left:0; right:0">SEARCH</base-button>
        </div>
        <div>
        <base-button class="animation-on-hover" type="default" style="display:block;margin:auto;  left:0; right:0">SEARCH </base-button>
        </div>
    
      </template>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content @click.native="toggleSidebar">

      </dashboard-content>

      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss">
</style>
<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
export default {
  components: {
    TopNavbar,

    ContentFooter,
    DashboardContent,
    MobileMenu
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    }
  }
};
</script>
