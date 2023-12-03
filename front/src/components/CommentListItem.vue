<template>
    <div>
        <!-- {{ comment }} - {{ comment.user.username }} -->
        <!-- <RouterLink :to="{ name: 'detail', params: { id: article.id }}">-->
        <p>
            {{ comment.content }}
            <button
                type="button"
                @click="deleteComment(comment.id)">삭제</button>
        </p>
        <hr>
    </div>
</template>
    
<script setup>
import { RouterLink } from 'vue-router';
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';


const counterStore = useCounterStore()
const props = defineProps({
comment: Object
})

const deleteComment = function (commentId) {
    axios({
      method: 'delete',
      url:  `${ counterStore.API_URL}/api/v1/articles/comments/${commentId}/`,
    })
      .then((res) =>{
        console.log(res)
        location.reload()
      })
      .catch((err) => {
        console.log('실패')
        console.log(err)
      })
  }
// deleteComment(comment)
onMounted(() => {
    console.log('comment', props.comment)
}
)



</script>