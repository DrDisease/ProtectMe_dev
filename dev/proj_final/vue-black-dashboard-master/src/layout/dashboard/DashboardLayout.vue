<template>
  <div class="wrapper">
    <side-bar>
      <template slot="links">
        <br>
        <br>
        <div>
          <a href = /#/searchtopico>
          <base-button class="animation-on-hover" type="default" style="display:block;  margin:auto;  left:0; right:0">SEARCH TOPIC</base-button>
          </a>
        </div>
        <br>
        <br>
        <div>
          <a href = /#/searchtweet>
          <base-button class="animation-on-hover" type="default" style="display:block;margin:auto;  left:0; right:0">SEARCH TWEET</base-button>
          </a>
        </div>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>

        <div>
          <a href = /#/about>
          <base-button class="animation-on-hover" type="warning" style="display:block; margin:auto;  left:0; right:0">ABOUT </base-button>
          </a>
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
