<template>
    <form>
        <div>
            통화 선택 1 :
            <select v-model="selected1">
                <option disabled value="">다음 중 하나를 선택하세요.</option>
                <option v-for="ex1 in exchange" v-bind:key="ex1.id">{{ ex1.cur_nm }}</option>
            </select>
            <input type="text" v-model="inputs">
            
            통화 선택 2 :
            <select v-model="selected2">
                <option disabled value="">다음 중 하나를 선택하세요.</option>
                <option v-for="ex2 in exchange" v-bind:key="ex2.id">{{ ex2.cur_nm }}</option>
            </select>
            <button @click.prevent="calculation">검색</button>
            <p>결과 : {{ submit }}</p> 
    
        </div>
    </form>
  </template>
  
<script setup>
  import axios from 'axios';
  import { ref, computed } from 'vue';
  
  const selected1 = ref('')
  const selected2 = ref('')

  const inputs = ref()
  const submit = ref()
  const result = ref()
  
  const calculation = () => {
    axios.get(`http://127.0.0.1:8000/exchanges/cal_exchange/${selected1.value}/${selected2.value}/`)
    .then((response) => {
        // data[0] -> 리스트 형태로 오니까 data[0]을 꼭 해줘야 함!!!!!!!!
        result.value = response.data[0].result
        submit.value = parseFloat(inputs.value) * result.value
    }).catch((error) => {
        console.log(error)
    })
  }
  
  const exchange = ref()

  axios.get(`http://127.0.0.1:8000/exchanges/get_exchange/`)
    .then((response) => {
        exchange.value = response.data
    }).catch((error) => {
        console.log(error)
    })

  
  </script>