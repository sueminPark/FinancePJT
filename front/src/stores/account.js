import { ref, computed } from 'vue'
import { acceptHMRUpdate, defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useAccountStore = defineStore('account', () => {

  const router = useRouter()

  const token = ref()
  const currUser = ref()

  const API_URL = 'http://127.0.0.1:8000'

  const signUp = (payload) => {
    axios.post(`${API_URL}/accounts/signup/`,{
        username: payload.username,
        email: payload.email,
        age: payload.age,
        money: payload.money,
        salary: payload.salary,
        nickname: payload.nickname,
        password1: payload.password1,
        password2: payload.password2,
    })
    .then(res => router.push({ name:'home'}))
    .catch(err => console.log(err))
}

  const login = (payload) => {
    axios.post(`${API_URL}/accounts/login/`, {
      username: payload.username,
      password: payload.password,
    }).then((res) => {
      console.log('로그인 완료!')
      token.value = res.data.key
      getUser()
      router.push({ name:'home' })
    }).catch((err) => {
      console.log(err)
    })
  }
  
  const logout = () => {
    token.value = null
    currUser.value = null
    console.log('로그아웃 완료!')
    // axios.post(`${API_URL}/accounts/logout/`)
    // .then((res) => {
    //   console.log('로그아웃 완료!') 
    // }).catch((err) => {
    //   console.log(err)
    // })
  }

  const getUser = () =>{
    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    }).then((res) => {
      axios.get(`${API_URL}/api/accounts/${res.data.pk}/`)
       .then((res) => {
        currUser.value = res.data
       }).catch((err) => {
        console.log(err)
       })
    }).catch((err) => {
      console.log(err)
    })

  }

  const updateUser = (user_pk, payload) => {
    axios.put(`${API_URL}/api/accounts/update/${user_pk}/`, payload, {
      headers: {
        'Authorization': `Token ${token.value}`,
      },
    })
      .then((res) => {
        getUser()
      }) .catch((err) => {
        console.log(err)
      })
    
  }

  const isLogin = computed(() => {
    if (token.value) {
      return true
    } else {
      return false
    }
  })

  return { signUp, login, logout, getUser, updateUser, currUser, isLogin, token }
}, { persist: true })
