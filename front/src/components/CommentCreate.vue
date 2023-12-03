<template>
    <div>
       <h3>댓글 쓰기</h3>            
   
       <div>
           <input type="text" class="form-control" v-model="comment" />
           <button type="button" class="btn btn-primary" @click="createComment">댓글 추가</button>
       </div>
   </div>
</template>
   
<script setup>
import { RouterLink } from 'vue-router';
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useAccountStore} from '@/stores/account'
import { useRouter, useRoute } from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const route = useRoute()
const accountStore = useAccountStore()

const comment = ref()

// const newComment = ref('')


const createComment = function () {
    axios({
        method : 'post',
        url: `${store.API_URL}/api/v1/articles/${route.params.id}/comments/`,
        data: {
            article: route.params.id,
            user: accountStore.currUser.id,
            content: comment.value,
        },
        headers: {
            Authorization:`Token ${accountStore.token}`
        }
    }).then((res) => {
        console.log('댓글 생성 완료!')
        location.reload()
    }).catch((err) => {
        console.log(err)
    })
}
   
// onMounted(() => {
//     axios({
//         method: 'get',
//         url: `${store.API_URL}/api/v1/articles/${route.params.id}/comments/`,
//     })
//         .then((res) => {
//             console.log('ㅋ')
//         // router.push({ name: 'detail'})
//         })
//         .catch((err) => {
//         console.log(err)
//         })
//     })

</script>

<style scoped>

</style>