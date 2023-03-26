<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
//import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header class='superior'>
  <nav class='superior_login'>
   <h2 class='login_logo'>Oraculo</h2>
   <div class='search'>
  <form action="/result" method="get">
   <input type="text" name="search" class='search_bar' id="srch"  placeholder='buscar' >
   <button>buscar</button>
  </form>
   </div>
  </nav>
  </header>
  <div class="body-page">
  <div class="shares"><div id="symbol"></div><p id ="price"><p id ="quote"></p></p><p id="exchange"></p><p id="cap"></p><p id="sec"><p id="inc"></p></p></div>
  <div id="plot_border" class='plot'><div id="plot_size" ></div><img id="plot_analisis" src="https://static.vecteezy.com/system/resources/previews/000/545/973/non_2x/bar-graph-vector-icon.jpg" alt=""></div>      
  <div class='description'><div id="name"></div ><div id="profile"></div></div>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
