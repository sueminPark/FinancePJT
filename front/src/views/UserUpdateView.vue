<template>
  <div>
      <h1>회원 정보 수정</h1>
      <form @submit.prevent="updateUser">
          <p>
              <label for="username">이름 : </label>
              <input type="text" name="" id="username" v-model.trim="username">
          </p>   
          <p>
              <label for="email">이메일 : </label>
              <input type="text" name="" id="email" v-model.trim="email">
          </p>
          <p>
              <label for="age">나이 : </label>
              <input type="text" name="" id="age" v-model.trim="age">
          </p>
          <p>
              <label for="money">자산 : </label>
              <input type="text" name="" id="money" v-model.trim="money">
          </p>
          <p>
              <label for="salary">수입 : </label>
              <input type="text" name="" id="salary" v-model.trim="salary">
          </p>
          <p>
              <label for="nickname">닉네임 : </label>
              <input type="text" name="" id="nickname" v-model.trim="nickname">
          </p>

          <p>
              <label for="password">기존 비밀번호 : </label>
              <input type="password" name="" id="password1" v-model.trim="password" required>
          </p>
 
          <button>회원 정보 수정</button>
      </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios'
import { useAccountStore } from '../stores/account';
import router from '../router';


const accountStore = useAccountStore()
const currUser = accountStore.currUser

const username = ref(currUser.username)
const email = ref(currUser.email)
const age = ref(currUser.age)
const money = ref(currUser.money)
const salary = ref(currUser.salary)
const nickname = ref(currUser.nickname)
const password = ref()


const updateUser = () => {
  const payload = {
      username: username.value,
      email: email.value,
      age: age.value,
      money: money.value,
      salary: salary.value,
      nickname: nickname.value,
      password: password.value,
  }
  accountStore.updateUser(currUser.id, payload)
  router.push({name:'mypage'})
}

</script>

<style scoped>

</style>