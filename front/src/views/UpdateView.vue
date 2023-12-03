<template>
    <div>
        <h1>게시글 수정</h1>
        <form @submit.prevent="updateArticle">
        <div>
            <label for="title">제목: </label> 
            <input v-model.trim="title" type="text" id="title">
        </div>
        <div>
            <label for="content">내용: </label>
            
            <textarea v-model.trim="content" id="content" ></textarea>
        </div>
        <button>수정 완료</button>
        </form>
    </div>
</template>


<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useAccountStore } from '@/stores/account'
import { useRouter, useRoute } from 'vue-router'

const title = ref(null)
const content = ref(null)
const article = ref(null)
const store = useCounterStore()
const accountStore = useAccountStore()
const router = useRouter()
const route = useRoute()

axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
})
    .then((res) => {
    // console.log(res.data)
    article.value = res.data
    title.value = article.value.title
    content.value = article.value.content
    })
    .catch((err) => {
    console.log(err)
    })


const updateArticle = function () {
    console.log(route.params.id)
    console.log(store.API_URL)
    axios({
        method: 'put',
        url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
        data: {
        title: title.value,
        content: content.value
        },
        headers: {
            Authorization: `Token ${accountStore.token}`
        }})
    
    .then((res) => {
    console.log(res)
    router.push({ name: 'detail' })
    })
    .catch((err) => {
    console.log(err)
    })
    }

    
</script>

<style>

</style>