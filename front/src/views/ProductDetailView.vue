<template>
  <div>
    <h1>상품 상세 정보</h1>
    <div class="detail">
      <h2>{{ productStore.product.fin_prdt_nm }}</h2>
      <p>은행 : {{ productStore.product.kor_co_nm }}</p>
      <p>가입 대상 : {{ productStore.product.join_member }}</p>
      <p v-if="productStore.product.max_limit">최고 한도 : {{ productStore.product.max_limit }}</p>
      <p>저축 기간: {{ productStore.product.save_trm }}개월</p>
      <p>저축 금리 유형 : {{ productStore.product.intr_rate_type_nm }}</p>
      <p>저축 금리 : {{ productStore.product.intr_rate }}</p>
      <p>최고 우대 금리 : {{ productStore.product.intr_rate2 }}</p>
      <div v-if="accountStore.isLogin">
        <button @click="productStore.cartUpdate(accountStore.currUser.username, productStore.product.fin_prdt_nm)">{{ cartButton }}</button>
      </div>
    </div>
    
</div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import { useProductStore } from '@/stores/product'
import { useAccountStore } from '@/stores/account'
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute()
const productStore = useProductStore()
const accountStore = useAccountStore()



productStore.productDetail(route.params.fin_prdt_nm)
productStore.getCart(accountStore.currUser.username)


const myP = ref(JSON.parse(localStorage.getItem('product')).myProducts)
const pr = ref(JSON.parse(localStorage.getItem('product')).product)

const cartButton = ref(myP.value.filter((p) => p.id == pr.value.id).length ? '해지하기' : '가입하기')


</script>

<style scoped>

.detail {
  border: 1px solid lightgrey;
  border-radius: 20px;
  margin: 20px;
  padding: 20px;
  padding-left: 50px;
}

</style>