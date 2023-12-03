<template>
    <div>
        <div  @click="getDetail" class="product">
            <h2>{{ product.fin_prdt_nm }}</h2>
            <p>은행 : {{ product.kor_co_nm }}</p>
            <p>가입 대상 : {{ product.join_member }}</p>
            <p>저축 금리 유형 : {{ product.intr_rate_type_nm }}</p>
            <p>최고 우대 금리 : {{ product.intr_rate2 }}</p>
        </div>
    </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
const router = useRouter()

const props = defineProps({
    product:Object,
})

const getDetail = () => {
    router.push({ name: 'productDetail', params: { fin_prdt_nm: props.product.fin_prdt_nm }  })
}

</script>

<style scoped>

.product {
    border: 2px solid lightgrey;
    border-radius: 30px;
    margin: 20px;
    padding: 20px;
    color: black;
    background-color: white;
}

</style>