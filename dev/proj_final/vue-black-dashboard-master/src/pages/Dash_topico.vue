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
      Topic:
      <small class="text-muted">COVID19</small>
    </h3>
    
    <h3>
      Keywords:
      <small class="text-muted">India, Health, SARS, Ebola, Italy, USA, Russia, Modi Government, facemask, doubt, CNN, fakenews</small>
    </h3>

    <h3>
      Average Feeling:
      <small class="text-muted">Neutral</small>
    </h3>

     <h3>
      Average Likes:
      <small class="text-muted">35</small>
    </h3>

     <h3>
      Average Retweets:
      <small class="text-muted">20</small>
    </h3>

     <h3>
      Average Number of Comments:
      <small class="text-muted">Neutral</small>
    </h3>

    </card>
    
    <div class="row">
      <div class="col-12">
        
      </div>
    </div>
    <div class="row">
      <div class="col-lg-4" :class="{'text-right': isRTL}">
        
      </div>
      <div class="col-lg-4" :class="{'text-right': isRTL}">
        <card type="chart">
          <template slot="header">
            <h5>Percentagem tweets por Feeling</h5>
          </template>
          <div class="chart-area">
            <bar-chart style="height: 100%"
                       chart-id="blue-bar-chart"
                       :chart-data="blueBarChart.chartData"
                       :gradient-stops="blueBarChart.gradientStops"
                       :extra-options="blueBarChart.extraOptions">
            </bar-chart>
          </div>
        </card>
      </div>
      <div class="col-lg-4" :class="{'text-right': isRTL}">
        
      </div>
    </div>
    <div class="row">
      <div class="col-lg-6 col-md-12">
        
      </div>
      <div class="col-lg-6 col-md-12">
       
      </div>
    </div>
  </div>
</template>
<script>
  import LineChart from '@/components/Charts/LineChart';
  import BarChart from '@/components/Charts/BarChart';
  import * as chartConfigs from '@/components/Charts/config';
  import TaskList from './Dashboard/TaskList';
  import UserTable from './Dashboard/UserTable';
  import config from '@/config';
  import wordcloud from 'vue-wordcloud'

  export default {
    components: {
      wordcloud,
      LineChart,
      BarChart,
      TaskList,
      UserTable
    },
    data() {
      return {
        myColors: ['#591945', '#900c3f', '#c70039', '#cf5733', '#ffc300'],
      defaultWords: [{
          "name": "India",
          "value": 20
        },
        {
          "name": "Health",
          "value": 19
        },
        {
          "name": "SARS",
          "value": 15
        },
        {
          "name": "Ebola",
          "value": 15
        },
        {
          "name": "Italy",
          "value": 22
        },
         {
          "name": "USA",
          "value": 18
        },
         {
          "name": "Russia",
          "value": 12
        },
         {
          "name": "Government",
          "value": 11
        },
         {
          "name": "facemask",
          "value": 17
        },
         {
          "name": "doubt",
          "value": 15
        },
         {
          "name": "CNN",
          "value": 10
        },
         {
          "name": "fakenews",
          "value": 20
        },
      ],
        bigLineChart: {
          allData: [
            [100, 70, 90, 70, 85, 60, 75, 60, 90, 80, 110, 100],
            [80, 120, 105, 110, 95, 105, 90, 100, 80, 95, 70, 120],
            [60, 80, 65, 130, 80, 105, 90, 130, 70, 115, 60, 130]
          ],
          activeIndex: 0,
          chartData: null,
          extraOptions: chartConfigs.purpleChartOptions,
          gradientColors: config.colors.primaryGradient,
          gradientStops: [1, 0.4, 0],
          categories: []
        },
        purpleLineChart: {
          extraOptions: chartConfigs.purpleChartOptions,
          chartData: {
            labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
            datasets: [{
              label: "Data",
              fill: true,
              borderColor: config.colors.primary,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.primary,
              pointBorderColor: 'rgba(255,255,255,0)',
              pointHoverBackgroundColor: config.colors.primary,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [80, 100, 70, 80, 120, 80],
            }]
          },
          gradientColors: config.colors.primaryGradient,
          gradientStops: [1, 0.2, 0],
        },
        greenLineChart: {
          extraOptions: chartConfigs.greenChartOptions,
          chartData: {
            labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV'],
            datasets: [{
              label: "My First dataset",
              fill: true,
              borderColor: config.colors.danger,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.danger,
              pointBorderColor: 'rgba(255,255,255,0)',
              pointHoverBackgroundColor: config.colors.danger,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [90, 27, 60, 12, 80],
            }]
          },
          gradientColors: ['rgba(66,134,121,0.15)', 'rgba(66,134,121,0.0)', 'rgba(66,134,121,0)'],
          gradientStops: [1, 0.4, 0],
        },
        blueBarChart: {
          extraOptions: chartConfigs.barChartOptions,
          chartData: {
            labels: ['Positive','Negative','Neutral'],
            datasets: [{
              label: "Countries",
              fill: true,
              borderColor: config.colors.info,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              data: [22,34,44],
            }]
          },
          gradientColors: config.colors.primaryGradient,
          gradientStops: [1, 0.4, 0],
        }
      }
    },
    computed: {
      enableRTL() {
        return this.$route.query.enableRTL;
      },
      isRTL() {
        return this.$rtl.isRTL;
      },
      bigLineChartCategories() {
        return this.$t('dashboard.chartCategories');
      }
    },
    methods: {
      initBigChart(index) {
        let chartData = {
          datasets: [{
            fill: true,
            borderColor: config.colors.primary,
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            pointBackgroundColor: config.colors.primary,
            pointBorderColor: 'rgba(255,255,255,0)',
            pointHoverBackgroundColor: config.colors.primary,
            pointBorderWidth: 20,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 15,
            pointRadius: 4,
            data: this.bigLineChart.allData[index]
          }],
          labels: ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
        }
        this.$refs.bigChart.updateGradients(chartData);
        this.bigLineChart.chartData = chartData;
        this.bigLineChart.activeIndex = index;
      }
    },
    mounted() {
      this.i18n = this.$i18n;
      if (this.enableRTL) {
        this.i18n.locale = 'ar';
        this.$rtl.enableRTL();
      }
      this.initBigChart(0);
    },
    beforeDestroy() {
      if (this.$rtl.isRTL) {
        this.i18n.locale = 'en';
        this.$rtl.disableRTL();
      }
    }
  };
</script>
<style>
</style>

