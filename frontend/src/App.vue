<script setup lang="ts">
import Login from './components/Login.vue';
// import Router from './components/Router.vue';
import { authData } from './store';
import { posts } from './actions/posts';
import NoteCallout from './components/NoteCallout.vue';
import Menu from './components/Menu.vue';

posts.fetchAll();
</script>

<template>
  <div class="w-screen min-h-screen bg-slate-600 text-white flex justify-center">
    <NoteCallout/>
    <div class="px-4">
      <Menu/>
    </div>
    <div class="lg:w-1/3 sm:w-1/2 w-full">
      <RouterView></RouterView>
    </div>
    <Login v-if="!authData.logged_in.value"/>
  </div>
</template>

<style>
</style>
