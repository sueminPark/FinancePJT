import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const articles = ref([])
  const comments = ref([])

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
        
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  const getComments = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/comments/`
    })
    .then((res) => {
      comments.value = res.data

    }).catch((err) => {
      console.log(err)
    })
  }

  // const deleteComment = function () {
  //   axios({
  //       method: 'delete',
  //       url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  //       data: {
  //       comment: comment.value,
        
  //       }
  //   })
  //   .then((res) => {
  //   console.log(res)
  //   router.push({ name: 'detail' })
  //   })
  //   .catch((err) => {
  //   console.log(err)
  //   })
  //   }

  // const updateArticles = function () {
  //   axios({
  //     method: 'get'
  //   })
  // }
  return { articles, API_URL, getArticles, comments, getComments }
}, { persist: true })