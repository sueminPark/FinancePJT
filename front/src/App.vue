<script setup>
import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAccountStore } from '@/stores/account'

const router = useRouter()
const accountStore = useAccountStore()

const logout = () => {
  accountStore.logout()
}

const getUser = () => {
  accountStore.getUser()
}

</script>

<template>
  <header>
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <RouterLink to="/"><img src="src/assets/shopping-cart.png" alt="logo.png"></RouterLink>
      </li>  
      
      <li class="nav-item">
        <RouterLink class="nav-link" :to="{ name: 'product'}">상품 목록</RouterLink>
      </li>  
      <li class="nav-item">
        <RouterLink class="nav-link" :to="{ name: 'map' }">내 주변 찾기</RouterLink>
      </li>  
      <li class="nav-item">
        <RouterLink class="nav-link" :to="{ name: 'exchange' }">환율</RouterLink>
      </li>
      <li class="nav-item">
        <RouterLink class="nav-link" :to="{ name: 'article'}">게시판</RouterLink>
      </li>  
        <template v-if="accountStore.isLogin">
          <li class="nav-item">  <RouterLink class="nav-link" :to="{ name:'mypage' }">마이페이지</RouterLink></li>
          <button @click="logout">로그아웃</button>
        </template>
        <template v-else>
          <RouterLink class="nav-link" :to="{ name: 'signup'}">회원가입</RouterLink>        
          <RouterLink class="nav-link" :to="{ name: 'login'}">로그인</RouterLink>
        </template>
    
    
      
    </ul>
  </header>

  <RouterView />
</template>

<style scoped>
a {
  margin: 20px;
  text-decoration: none;
  color: black;
}

.center {
    text-align: center;
}

img {
  position: relative;
  top: 6px;
  width: 25px;
  height: 25px;
}

</style>
