<template>
    <br>
    <div class="center">
        <h1>환율 계산</h1>
        <br>
        <ExchangeList />

    </div>
</template>

<script setup>
import ExchangeList from '@/components/ExchangeList.vue';

</script>

<style scoped>
.center {
    text-align: center;
}
</style>