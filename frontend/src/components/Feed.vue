<script setup lang="ts">
import { ref } from 'vue';
import Post from './Post.vue';
import NewPost from './NewPost.vue';
import { postsData } from '../store';

let followers = ref(true);

</script>

<template>
    <div class="lg:w-1/3 sm:w-1/2 w-full  h-10 flex items-center fixed backdrop-blur-xl">
        <button @click="followers = true"
        class="w-full hover:bg-slate-500 hover:bg-opacity-30 h-10" 
        :class="{'text-slate-400': !followers}">
            Following
        </button>
        <button @click="followers = false"
        class="w-full hover:bg-slate-500 hover:bg-opacity-30 h-10" 
        :class="{'text-slate-400': followers}">
            All
        </button>
    </div>
    <div class="lg:w-1/3 sm:w-1/2 bg-slate-800 w-full">
        <div class="h-10"></div>

        <NewPost/>
        <div class="max-w-[100%] overflow-clip">
            <div v-for="post in postsData.all">
                <Post :data="post"/>
            </div>
        </div>
    </div>
</template>