<template>
    <div>
        <h1>회원가입 페이지</h1>
        <form @submit.prevent="signUp">
            <p>
                <label for="username">username : </label>
                <input type="text" name="" id="username" v-model.trim="username">
            </p>   
            <p>
                <label for="email">email : </label>
                <input type="text" name="" id="email" v-model.trim="email">
            </p>
            <p>
                <label for="age">age : </label>
                <input type="text" name="" id="age" v-model.trim="age">
            </p>
            <p>
                <label for="money">money : </label>
                <input type="text" name="" id="money" v-model.trim="money">
            </p>
            <p>
                <label for="salary">salary : </label>
                <input type="text" name="" id="salary" v-model.trim="salary">
            </p>
            <p>
                <label for="nickname">nickname : </label>
                <input type="text" name="" id="nickname" v-model.trim="nickname">
            </p>

            <p>
                <label for="password1">password1 : </label>
                <input type="password" name="" id="password1" v-model.trim="password1">
            </p>
            <p>
                <label for="password2">password2 : </label>
                <input type="password" name="" id="password2" v-model.trim="password2">
            </p>
            <button>회원가입</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios'
import { useAccountStore } from '../stores/account';


const accountStore = useAccountStore()

const username = ref()
const email = ref()
const age = ref()
const money = ref()
const salary = ref()
const nickname = ref()
const password1 = ref()
const password2 = ref()

const signUp = () => {
    const payload = {
        username: username.value,
        email: email.value,
        age: age.value,
        money: money.value,
        salary: salary.value,
        nickname: nickname.value,
        password1: password1.value,
        password2: password2.value,
    }
    accountStore.signUp(payload)
}

</script>

<style scoped>

</style>