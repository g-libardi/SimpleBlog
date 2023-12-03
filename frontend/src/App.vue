<script setup lang="ts">
import Login from './components/Login.vue';
// import Router from './components/Router.vue';
import { authData } from './store';
import { posts } from './actions/posts';
import NoteCallout from './components/NoteCallout.vue';

posts.fetchAll();
</script>

<template>
  <div class="w-screen min-h-screen bg-slate-600 text-white flex justify-center">
    <NoteCallout/>
    <RouterView></RouterView>
    <Login v-if="!authData.logged_in.value"/>
  </div>
</template>

<style>
</style>
