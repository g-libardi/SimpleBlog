<script setup lang="ts">
import { Icon } from '@iconify/vue';
defineProps(['data']);
</script>

<template>
    <div class="flex border-b border-b-slate-600 mt-4">
        <div class="w-[50px] flex justify-center">
            <img class="mt-2 rounded-full w-[35px] h-[35px]" 
            src="https://picsum.photos/50/55" 
            alt="profile picture">
        </div>

        <div class="min-h-20 max-w-[calc(95%-50px)]">
            <div class="flex">
                <p class="font-bold leading-none mr-2">
                    {{ data.username }}
                </p>
                <p class="leading-none text-slate-400">
                    {{ data.created_at }}
                </p>
            </div>
            <p>
                {{ data.content }}
            </p>
            <div class="flex mt-2 mb-4">
                <button class="text-slate-400 hover:text-slate-300 flex items-center mr-6">
                    <Icon icon="akar-icons:comment" class="w-5 h-5 mr-1"/>
                    <p>0 replies</p>
                </button>
                <button class="text-slate-400 hover:text-slate-300 flex items-center">
                    <Icon icon="akar-icons:heart" class="w-5 h-5 mr-1"/>
                    <p>0 likes</p>
                </button>
            </div>
        </div>
    </div>
</template>