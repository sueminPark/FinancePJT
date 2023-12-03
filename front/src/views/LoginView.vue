<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="login">
      <p>
        <label for="username">아이디 : </label>
        <input type="text" id="username" v-model="username">
      </p>
      <p>
        <label for="password">비밀번호 : </label>
        <input type="password" id="password" v-model="password">
      </p>
      <button>로그인</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAccountStore } from '@/stores/account'

const router = useRouter()
const accountStore = useAccountStore()

const username = ref()
const password = ref()

const login = () => {
  const payload = {
    username: username.value,
    password: password.value,
  }
  accountStore.login(payload)
}

</script>

<style scoped>

</style>