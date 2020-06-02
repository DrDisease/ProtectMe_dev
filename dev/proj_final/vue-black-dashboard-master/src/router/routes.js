import DashboardLayout from "@/layout/dashboard/DashboardLayout.vue";
// GeneralViews
import NotFound from "@/pages/NotFoundPage.vue";

// Admin pages

const Initial = () => import(/* webpackChunkName: "initial" */"@/pages/Initial.vue");
const Dash_tweet = () => import(/* webpackChunkName: "tweet" */"@/pages/Dash_tweet.vue");
const Search_topico = () => import(/* webpackChunkName: "searchtopico" */"@/pages/Search_topico.vue");
const Search_tweet = () => import(/* webpackChunkName: "searchtweet" */"@/pages/Search_tweet.vue");
const Dash_topico = () => import(/* webpackChunkName: "topico" */"@/pages/Dash_topico.vue");
const About = () => import(/* webpackChunkName: "about" */"@/pages/About.vue");
const Dashboard = () => import(/* webpackChunkName: "dashboard" */"@/pages/Dashboard.vue");
const Profile = () => import(/* webpackChunkName: "common" */ "@/pages/Profile.vue");
const Notifications = () => import(/* webpackChunkName: "common" */"@/pages/Notifications.vue");
const Icons = () => import(/* webpackChunkName: "common" */ "@/pages/Icons.vue");
const Maps = () => import(/* webpackChunkName: "common" */ "@/pages/Maps.vue");
const Typography = () => import(/* webpackChunkName: "common" */ "@/pages/Typography.vue");
const TableList = () => import(/* webpackChunkName: "common" */ "@/pages/TableList.vue");

const routes = [
  {
    path: "/",
    name: "home",
    redirect: "/initial",
    component: DashboardLayout,
    children: [
      {
        path: "initial",
        name: "initial",
        component: Initial
      },
      {
        path: "searchtweet",
        name: "searchtweet",
        component: Search_tweet
      },
      {
        path: "searchtopico",
        name: "searchtopico",
        component: Search_topico
      },
      {
        path: "tweet",
        name: "tweet",
        component: Dash_tweet
      },
      {
        path: "topico",
        name: "topico",
        component: Dash_topico
      },
      {
        path: "about",
        name: "about",
        component: About
      },
      {
        path: "dashboard",
        name: "dashboard",
        component: Dashboard
      },
      {
        path: "profile",
        name: "profile",
        component: Profile
      },
      {
        path: "notifications",
        name: "notifications",
        component: Notifications
      },
      {
        path: "icons",
        name: "icons",
        component: Icons
      },
      {
        path: "maps",
        name: "maps",
        component: Maps
      },
      {
        path: "typography",
        name: "typography",
        component: Typography
      },
      {
        path: "table-list",
        name: "table-list",
        component: TableList
      }
    ]
  },
  { path: "*", component: NotFound },
];

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/

export default routes;
