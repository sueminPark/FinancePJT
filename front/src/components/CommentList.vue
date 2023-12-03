<template>
    <div>
        <h3>댓글 목록</h3>
            <!-- <div v-if="comments.length"> -->
                    <!-- <li v-for="(comment, index) in comments" :key="comment.id"> -->
                    <!-- {{ comment }} - {{ comment.user.username }} --> 
                <CommentListItem 
                v-for="comment in store.comments"
                :key="comment.id"
                :comment="comment" />
    
            <!-- </div> -->
        
    </div>
</template>
    
<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useAccountStore } from '@/stores/account'

import CommentListItem from '@/components/CommentListItem.vue'
import axios from 'axios';

const store = useCounterStore()
const accountStore = useAccountStore()
store.getComments()
// const comments = ref()

console.log(store.comments)

const test = function () {
    store.getComments() 
    // axios({
    //     method: 'get',
    //     url: `${store.API_URL}/api/v1/articles/comments/`,
    // }).then((res) => {
    //     console.log('success', res)
    //     // accountStore.comments = res.data
    //     comments.value = res.data
    //     console.log(comments.value)
    //     // router.push({ name: 'article' })
    // }).catch((err) => {
    //     console.log(err)
    // })

    console.log(accountStore.comments)
}

</script>

<style>
</style>