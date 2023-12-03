<template>
    <div class="products">
        <div>
            <h1>은행 선택</h1>
            <select v-model="selectedBank" class="select" multiple>
                <option>전체</option>
                <option v-for="bank in bankList" >{{ bank }}</option>
            </select>
        </div>
        <div class="productList">
            <h1>예금 목록</h1>
            <div class="product">
                <div v-if="depositList.length">
                    <ProductList v-for="deposit in depositList" :product="deposit"/>
                </div>
                <div v-else>
                    <p>해당 조건의 예금이 없습니다.</p>
                </div>
            </div>
        </div>
        <div class="productList">
            <h1>적금 목록</h1>
            <div class="product">
                <div v-if="savingList.length">
                    <ProductList v-for="saving in savingList" :product="saving"/>
                </div>
                <div v-else>
                    <p>해당 조건의 적금이 없습니다.</p>
                </div>
            </div>
        </div>        
   
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import ProductList from '@/components/ProductList.vue'
import axios from 'axios';
import { useProductStore } from '@/stores/product'

// 미리 저장해 놓은 응답 json 파일 불러와서 활용
// import savingList from '@/assets/savingList'
// import depositList from '@/assets/depositList'

const productStore = useProductStore()

const depositList = ref()
const allDepositList = ref()
const savingList = ref()
const allSavingList = ref()
const selectedBank = ref()
const bankList = productStore.bankList



axios.get('http://127.0.0.1:8000/api/v1/get_deposit/')
.then((response) => {
    depositList.value = response.data
    allDepositList.value = response.data
}).catch((error) => {
    console.log(error)
})

axios.get('http://127.0.0.1:8000/api/v1/get_saving/')
.then((response) => {
    savingList.value = response.data
    allSavingList.value = response.data
}).catch((error) => {
    console.log(error)
})

productStore.getBank()

watch(selectedBank, (newValue, oldValue) =>{
    if (!newValue.includes('전체')) {
        depositList.value = []
        savingList.value = []
        for (let sel of newValue){
            depositList.value = depositList.value.concat(allDepositList.value.filter((product) => product.kor_co_nm == sel))
            savingList.value = savingList.value.concat(allSavingList.value.filter((product) => product.kor_co_nm == sel))            
        }
    }
    else {
        depositList.value = allDepositList.value
        savingList.value = allSavingList.value
    }
})


// // 각 응답 상품 갯수
// const juck_cnt = savingList.result.total_count

// // 각 응답
// const juck = savingList.result

</script>

<style scoped>
h1 {
    text-align: center;
}

.select {
    height: 80vh;
}
.products {
    display: flex;
    justify-content: center;
}

.productList {
    width: 100%;
}

.product {
    border: 1px solid lightgrey;
    margin: 10px;
    overflow: scroll;
    height: 80vh;
}

/* .productList {
    border: 1px solid lightgrey;
    border-radius: 20px;
    margin: 20px;
    margin-top: 30px;
    padding: 20px;
} */



</style>