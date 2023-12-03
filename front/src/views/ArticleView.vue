<template>
    <div>
        <h1>자유 게시판</h1>
        <RouterLink :to="{ name: 'create' }">
        [CREATE]
        </RouterLink>
        <ArticleList />
    </div>
</template>

<script setup>
    import { onMounted } from 'vue'
    import { useCounterStore } from '@/stores/counter'
    import { RouterLink } from 'vue-router'
    import ArticleList from '@/components/ArticleList.vue'

    const store = useCounterStore()

    onMounted(() => {
    store.getArticles()
    })

</script>

<style>

</style>