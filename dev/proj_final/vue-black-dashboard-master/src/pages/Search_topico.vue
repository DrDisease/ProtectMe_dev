<template>
  <div>
  <card>
      <form @submit.prevent>
        <base-input label="Search Topic:"
                    type="topic_link"
                    placeholder="Enter topic">
            <small slot="helperText" id="emailHelp" class="form-text text-muted">Eg: portugal, europe, corona, riot...</small>
        </base-input>
      <a href= /#/topico>
      <!--<base-button v-on:click="tweetTopico" class="animation-on-hover" type="primary" style="display:block; ">SEARCH TOPIC</base-button> -->
      <button v-on:click="getTweetTopico"> This shit here</button>
      {{tweetTopic}}
      </a>
      </form>
  </card>
  <img src="../assets/img/us_wine.png" style="position: absolute;margin: auto;top: 0;left: 240px;right: 0;bottom: -200px;">
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'searchtopico',
  components(){
     
  },
  data() {
    return {
      tweetTopic : [],
    };
  },
  methods: {
    getTweetTopico(){
      axios.get("http://127.0.0.1:8000/api/tweetTopic/", {
        params:{
          tweetTopic: this.tweetTopic
        } 
      })
      .then(res => (this.tweetTopic = res.data))
      .catch(err => console.log(err));
      console.log(this.tweetTopic)
    }
  },
  created(){
    this.getTweetTopico()
  }
};
</script>
<style></style>