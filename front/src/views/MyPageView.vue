<template>
  <div>
    <div v-if="accountStore.currUser" class="userDetail">
      <h1>{{ accountStore.currUser.username }}님의 페이지</h1>
      <p>닉네임 : {{ accountStore.currUser.nickname }}</p>      
      <p>나이 : {{ accountStore.currUser.age }}</p>      
      <p>이메일 : {{ accountStore.currUser.email }}</p>      
      <p>자산 : {{ accountStore.currUser.money }}</p>      
      <p>수입 : {{ accountStore.currUser.salary }}</p>
      <button @click="updateUser">회원 정보 수정</button>
      <div class="productInfo">
        <div class="pContainer">
          <div class='pItem' >
            <p class="pList"><b>최대 저축 금리 상품 추천</b></p>
              <div v-for="idx in 5" @click="productDetail(notMine[idx-1])" class="pLink">{{ notMine[idx-1].fin_prdt_nm }}</div>
          </div>
          <div class="pItem myList">
            <p class="pList"><b>가입 상품 목록</b></p>
            <div v-for="product in productStore.myProducts">
              <div class="pLink" @click="productDetail(product)">{{ product.fin_prdt_nm }}</div>
            </div>
          </div>
        </div>
        </div>
      <div class="chart">
        <h3>가입 예금 금리 비교</h3>
        <canvas id="depositChart"></canvas>
      </div>
      <div class="chart">
        <h3>가입 적금 금리 비교</h3>
        <canvas id="savingChart"></canvas>
      </div>
    </div>
    <div v-else>
      <h1>로그인을 하지 않았습니다.</h1>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useAccountStore } from '@/stores/account'
import { useProductStore } from '@/stores/product'
import ProductList from '@/components/ProductList.vue';
import Chart from 'chart.js/auto'

const route = useRoute()
const router = useRouter()
const accountStore = useAccountStore()
const productStore = useProductStore()

productStore.getCart(accountStore.currUser.username)
productStore.getBank()

const allProducts = ref([...productStore.allProducts])
allProducts.value.sort((a,b) => b.intr_rate-a.intr_rate)
const notMine = ref(allProducts.value.filter(p => !JSON.parse(localStorage.product).myProducts.filter((p2) => p2.id == p.id).length))


const myDepositName = ref([])
const myDepositRate = ref([])
const mySavingName = ref([])
const mySavingRate = ref([])


const productDetail = (product) => {
  router.push({name:'productDetail', params:{fin_prdt_nm: product.fin_prdt_nm}})
}

const updateUser = () => {
  router.push({name:'updateUser'})
}





let depositChart;
let savingChart;

onMounted(() => {
  for (let product of productStore.myProducts){
    if (product.prdt_div === "D"){
      myDepositName.value.push(product.fin_prdt_nm)
      myDepositRate.value.push(product.intr_rate)
    } else {
      mySavingName.value.push(product.fin_prdt_nm)
      mySavingRate.value.push(product.intr_rate)
    }
  }
  
  console.log(myDepositName.value)
  console.log(myDepositRate.value)
  
  const depositChartData = {
    labels: myDepositName.value,
    datasets: [
      {
        label: '저축 금리',
        data: myDepositRate.value,
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
      },
    ],
  }

  const savingChartData = {
    labels: mySavingName.value,
    datasets: [
      {
        label: '저축 금리',
        data: mySavingRate.value,
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
      },
    ],
  }

  const dCtx = document.getElementById('depositChart').getContext('2d');
  const sCtx = document.getElementById('savingChart').getContext('2d');

  depositChart = new Chart(dCtx, {
    type: 'bar',
    data: depositChartData,
  });

  savingChart = new Chart(sCtx, {
    type: 'bar',
    data: savingChartData,
  });

});



</script>

<style scoped>
.userDetail {
 margin: 50px;
 border: 1px solid lightgrey;
 border-radius: 20px;
 padding: 20px;
 padding-left: 50px;
}

.chart {
  border: 1px solid lightgrey;
  margin: 20px;
}

h3 {
  text-align: center;
}

.pContainer {
  display: flex;
}

.pItem {
  width: 50%;
}

.pLink {
  border: 1px solid lightgrey;
  padding: 20px;
  margin: 10px;
  border-radius: 10px;
}

a {
  text-decoration: none;
  color: black;
}

.myList {
  overflow: scroll;
}

.pList {
  text-align: center;
}
</style>
