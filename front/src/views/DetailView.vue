<template>
    <div>
        <h1>Detail</h1>
        <div v-if="article">
            <p>제목 : {{ article.title }}</p>
            <p>내용 : {{ article.content }}</p>
            <p>작성일 : {{ article.created_at }}</p>
            <p>수정일 : {{ article.updated_at }}</p>
            <RouterLink :to="{ name: 'update' }">[수정하기]</RouterLink>  |  
            <button @click="deleteArticle">[삭제하기]</button> 
         
        <CommentCreate />
        <CommentList />
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRoute, useRouter } from 'vue-router';
import CommentCreate from '@/components/CommentCreate.vue';
import CommentList from '@/components/CommentList.vue';

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)

// deleteArticle()

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
    }).then((res) => {
        article.value = res.data
        // router.push({ name: 'detail'})
    }).catch((err) => {
        console.log(err)
    })

})

const deleteArticle = function () {
    axios({
        method: 'delete',
        url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
        data: {
        article: article.value
        }
    }).then((res) => {
        console.log(res)
        router.push({ name: 'article' })
    }).catch((err) => {
        console.log(err)
    })
}




</script>
    
<style>
    
</style>