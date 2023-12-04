<script setup lang="ts">
import { Icon } from '@iconify/vue/dist/iconify.js';
</script>

<template>
    <div class="text-2xl">
        <h1 class="text-2xl font-bold px-2 pb-2 pt-1">
            SimpleBlog
        </h1>
        <RouterLink to="/" class="flex items-center p-2 rounded-full hover:bg-opacity-20 hover:bg-white"
        :class="{'font-bold': $route.path === '/'}">
            <Icon icon="majesticons:home-line" class="w-5 h-5 mr-1" v-if="$route.path !== '/'"/>
            <Icon icon="majesticons:home" class="w-5 h-5 mr-1" v-else/>
            <p>Feed</p>
        </RouterLink>
        <RouterLink to="/profile" class="flex items-center p-2 rounded-full hover:bg-opacity-20 hover:bg-white"
        :class="{'font-bold': $route.path === '/profile'}">
            <Icon icon="fluent:person-12-regular" class="w-5 h-5 mr-1" v-if="$route.path !== '/profile'"/>
            <Icon icon="fluent:person-12-filled" class="w-5 h-5 mr-1" v-else/>
            <p>Profile</p>
        </RouterLink>
    </div>
</template>