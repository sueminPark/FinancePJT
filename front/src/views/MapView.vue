<template>
    <div class="center">
        <h1><img src="src/assets/pin.png" alt="pin.png">내 주변 은행 찾기</h1>
        <KakaoMap />
    </div>
</template>

<script setup>
import KakaoMap from '@/components/KakaoMap.vue';
</script>

<style scoped>
.center {
    text-align: center;
}

img {
  position: relative;
  top: 15px;
  width: 50px;
  height: 50px;
}
</style>