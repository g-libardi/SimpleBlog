<script setup lang="ts">
    import { auth } from '../actions/auth';
    import { ref } from 'vue';

    const option = ref(0);
    let name = ref('');
    let username = ref('');
    let password = ref('');
    let confirm_password = ref('');
    // login('TestUser', 'password');
</script>

<template>
  <div class="z-10 bg-black bg-opacity-60 backdrop-blur-sm fixed w-screen h-screen flex items-center justify-center">
    <div class="bg-slate-600 pt-0 rounded-2xl">
      <div class="w-100 flex justify-evenly mb-3">
        <button @click="option = 0"
        :class="{'bg-slate-800': option}" class="hover:bg-slate-700 w-full p-1 rounded-tl-2xl">
          Login
        </button>
        <button @click="option = 1"
        :class="{'bg-slate-800': !option}" class="hover:bg-slate-700 w-full p-1 rounded-tr-2xl">
          Register
        </button>
      </div>
      
      <form @submit.prevent="() => auth.login(username, password)" 
        v-if="!option"
        class="flex flex-col m-7">
        <label for="username">Username</label>
        <input class="bg-slate-800 h-8 rounded-full pl-2 pr-2" type="text" id="username" v-model="username" />
        <label for="password">Password</label>
        <input class="bg-slate-800 h-8 rounded-full pl-2 pr-2" type="password" id="password" v-model="password" />
        <div class="flex">
          <button class="w-full border-r mt-3 rounded-s-full h-8 bg-sky-600 hover:bg-sky-500" type="submit">Login</button>
          <button class="w-full border-l mt-3 rounded-e-full h-8 bg-sky-600 hover:bg-sky-500"
          @click.prevent="() => {username='TestUser'; password='password';}">
          Test User
          </button>
        </div>
      </form>
  
      <form @submit.prevent="() => auth.register(name, username, password)"
        v-else
        class="flex flex-col m-7">
        <label for="name">Name</label>
        <input class="bg-slate-800 h-8 rounded-full pl-2 pr-2" type="text" id="name" v-model="name" />
        <label for="username">Username</label>
        <input class="bg-slate-800 h-8 rounded-full pl-2 pr-2" type="text" id="username" v-model="username" />
        <label for="password">Password</label>
        <input class="bg-slate-800 h-8 rounded-full pl-2 pr-2" type="password" id="password" v-model="password" />
        <label for="password">Confirm Password</label>
        <input class="bg-slate-800 h-8 rounded-full pl-2 pr-2" type="password" id="confirm-password" v-model="confirm_password" />
        <button class="mt-3 rounded-full h-8 bg-sky-600 hover:bg-sky-500" type="submit">Register</button>
      </form>
    </div>
    

  </div>
</template>

<style scoped>
</style>