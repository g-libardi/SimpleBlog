<script setup lang="ts">
import { ref } from 'vue';
import Post from '../components/Post.vue';
import NewPost from '../components/NewPost.vue';
import { postsData } from '../store';

let followers = ref(true);
const allPosts = postsData.all;

</script>

<template>
    <div class="bg-slate-800">
        <div class="w-full h-10 flex items-center backdrop-blur-md sticky top-0">
        <button @click="followers = true"
        class="w-full hover:bg-slate-500 hover:bg-opacity-30 h-12" 
        :class="{'text-slate-400': !followers}">
            Following
        </button>
        <button @click="followers = false"
        class="w-full hover:bg-slate-500 hover:bg-opacity-30 h-12" 
        :class="{'text-slate-400': followers}">
            All
        </button>
        </div>
        <div class="w-full">
            <NewPost class="mt-2"/>
            <div class="max-w-[100%] overflow-clip">
                <div v-for="post in allPosts">
                    <Post :data="post"/>
                </div>
            </div>
        </div>
    </div>
</template>