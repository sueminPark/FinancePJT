<template>
    <div>
        <!-- <h5>{{ article.id }}</h5> -->
        <strong><h5>{{ article.title }}</h5></strong>
        <p>{{ article.content }}</p>
        <RouterLink :to="{ name: 'detail', params: { id: article.id }}">
        [Detail]
        </RouterLink>
        <hr>
    </div>
</template>
    
<script setup>
import { RouterLink } from 'vue-router';

defineProps({
article: Object
})
</script>