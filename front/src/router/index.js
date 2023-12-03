import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MyPageView from '@/views/MyPageView.vue'
import ProductView from '@/views/ProductView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import MapView from '@/views/MapView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import ArticleView from '@/views/ArticleView.vue'
import CreateView from '@/views/CreateView.vue'
import DetailView from '@/views/DetailView.vue'
import UpdateView from '@/views/UpdateView.vue'
import UserUpdateView from '@/views/UserUpdateView.vue'

import { useAccountStore } from '@/stores/account'




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/mypage',
      name: 'mypage',
      component: MyPageView
    },
    // 한페이지에서 보여줄 것이므로 예아뷰와 적뷰를 통합
    {
      path: '/product',
      name: 'product',
      component: ProductView
    },
    {
      path: '/product/:fin_prdt_nm',
      name: 'productDetail',
      component: ProductDetailView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/updatUser',
      name: 'updateUser',
      component: UserUpdateView
    },
    {
      path: '/artricle',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: DetailView
    },
    {
      path: '/create',
      name: 'create',
      component: CreateView
    },
    {
      path: '/update/:id',                                                    
      name: 'update',
      component: UpdateView
    }, 
    
  
  ]
})

router.beforeEach((to, from) =>{
  const loginRequiredName = ['mypage', 'updateUser', 'update', 'create']
  const logoutRequiredName = ['signup', 'login']
  const accountStore = useAccountStore()
  if (loginRequiredName.includes(to.name) && !accountStore.isLogin){
    window.alert('로그인이 필요합니다.')
    return { name:'login' }
  }
  else if (logoutRequiredName.includes(to.name) && accountStore.isLogin){
    window.alert('이미 로그인되어 있습니다.')
    return { name : from.name }
  }
})

export default router
