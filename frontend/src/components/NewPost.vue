<script setup lang="ts">
import { ref } from 'vue';
import { posts } from '../actions/posts';

let content = ref('');
let textbox = ref(null as HTMLDivElement | null);

async function send_post() {
    if (await posts.publish(content.value)) {
        content.value = '';
        if (textbox.value) textbox.value.innerText = '';
    }
}

</script>

<template>
  <div class="w-full flex border-b border-b-slate-500">
    <div class="w-[50px] w-min-[50px] flex justify-center">
        <img class="rounded-full w-[35px] h-[35px]" 
        src="https://picsum.photos/50/55" 
        alt="profile picture">
    </div>
    <div class="flex-grow max-w-[calc(95%-50px)] bg-slate-800">
        <div
        class=" outline-none flex-grow-0
        before:content-none max-w-prose whitespace-pre-wrap
        empty:before:content-['What\'s_happening?']
        empty:before:text-slate-400 cursor-text"
        role="textbox" contenteditable="true"
        @input="content = ($event.target as HTMLDivElement).innerText"
        ref="textbox">
        </div>

        <div class="my-4">
            <button class="bg-sky-600 rounded-full px-2 hover:bg-sky-700"
            @click="send_post">
                Send
            </button>
        </div>
    </div>
  </div>
</template>