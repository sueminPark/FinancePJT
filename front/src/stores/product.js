import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  
  const API_URL = 'http://127.0.0.1:8000'

  const product = ref('')
  const myProducts = ref([])
  const bankList = ref([])
  const allProducts = ref([])

  const getBank = () => {
    axios.get(`${API_URL}/api/v1/get_all/`)
    .then((res) => {
      allProducts.value = res.data
      bankList.value = []
      for (let i of res.data){
        if (!bankList.value.includes(i.kor_co_nm)) {
          bankList.value.push(i.kor_co_nm)
        }
      }
    }).catch((err) => {
      console.log(err)
    }) 
  }
  

  const productDetail = (fin_prdt_nm) => {    
    axios.get(`${API_URL}/api/v1/detail/${fin_prdt_nm}/`)
    .then((res) => {
      product.value = res.data
    }).catch((err) => {
      console.log(err)
    })    
  }

  const getCart = (username) => {
    axios.get(`${API_URL}/api/v1/cart/${username}/`)
    .then((res) => {
      myProducts.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }

  const cartUpdate = (username, fin_prdt_nm) => {
    axios.get(`${API_URL}/api/v1/cart/${username}/${fin_prdt_nm}/`)
    .then((res) => {
      myProducts.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }
  


  return { getBank, productDetail, getCart, cartUpdate, allProducts, myProducts, product, bankList }
}, {persist:true})
