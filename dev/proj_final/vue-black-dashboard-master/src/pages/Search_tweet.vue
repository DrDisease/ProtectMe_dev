<template>
  <div>
  <card>
      <form @submit.prevent>
        <base-input label="Search Tweet:"
                    type="tweet_link"
                    placeholder="Enter tweet link">
        </base-input>
      <a href= /#/tweet>
      <base-button class="animation-on-hover" type="primary" style="display:block; ">SEARCH TWEET</base-button>
      </a>
      </form>
  </card>
  <img src="../assets/img/us_wine.png" style="position: absolute;margin: auto;top: 0;left: 240px;right: 0;bottom: -200px;">
  </div>
</template>

<script>
export default {
  name: 'searchtweet',
  data() {
    return {};
  }
};
</script>
<style></style>