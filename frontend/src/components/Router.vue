<script setup lang="ts">
import { ref, computed } from 'vue'
import Login from './Login.vue';
import Feed from './Feed.vue';
import NotFound from './NotFound.vue';

const routes = {
  '/': Feed
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
  console.log(currentPath.value)
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] || NotFound
})
</script>

<template>
  <component :is="currentView" />
</template>