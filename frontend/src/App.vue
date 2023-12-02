<script setup lang="ts">
import Feed from './components/Feed.vue';
import Login from './components/Login.vue';
// import Router from './components/Router.vue';
import { authData } from './store';

</script>

<template>
  <div class="w-screen min-h-screen bg-slate-600 text-white flex justify-center">
    <Feed/>
    <Login v-if="!authData.logged_in"/>
  </div>
</template>

<style>
</style>
