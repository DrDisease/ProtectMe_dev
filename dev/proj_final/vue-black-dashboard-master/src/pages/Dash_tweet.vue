<template>
  <div>
    
    <div id="app">
        <wordcloud
        :data="defaultWords"
        nameKey="name"
        valueKey="value"
        :color="myColors"
        :showTooltip="true"
        :wordClick="wordClickHandler">
        </wordcloud>
    </div>
    
    <card>
    <h3>
      Keywords:
      <small class="text-muted">Government, hiding, covid19, India, incompetence</small>
    </h3>

    <h3>
      Topics:
      <small class="text-muted">COVID19, HEALTH</small>
    </h3>

    <h3>
      Likes:
      <small class="text-muted">1</small>
    </h3>

    <h3>
      Retweets:
      <small class="text-muted">4</small>
    </h3>

    <h3>
      Number of Comments:
      <small class="text-muted">0</small>
    </h3>

    <h3>
      Feeling:
      <small class="text-muted">Negative</small>
    </h3>

    <h3>
      Average Response Feeling:
      <small class="text-muted">Neutral</small>
    </h3>



    <h3>
      Text:
      <small class="text-muted">Modi government is deliberately hiding the real number of covid19 cases in India to hide its incompetence.</small>
    </h3>

    <h3>
      Image:
      <br>
       <img src="https://pbs.twimg.com/media/EZluOYOWoAAjNCh?format=jpg"  width="500" > 
        <h3>
          <small class="text-muted">Description: Person(Man 43 Years Old) behind curtains</small>
        </h3>
    </h3>
    </card>
    

    
  
  </div>
</template>

<script>
import wordcloud from 'vue-wordcloud'

export default {
  name: 'app',
  components: {
    wordcloud
  },
  methods: {
    wordClickHandler(name, value, vm) {
      console.log('wordClickHandler', name, value, vm);
    }
  },
  data() {
    return {
      myColors: ['#591945', '#900c3f', '#c70039', '#cf5733', '#ffc300'],
      defaultWords: [{
          "name": "Government",
          "value": 20
        },
        {
          "name": "hiding",
          "value": 19
        },
        {
          "name": "covid19",
          "value": 30
        },
        {
          "name": "India",
          "value": 15
        },
        {
          "name": "incompetence",
          "value": 10
        },
      ]
    }
  }
}
</script>
