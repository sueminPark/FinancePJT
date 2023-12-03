import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPuginPersistedstate from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPuginPersistedstate)

app.use(createPinia())
app.use(router)
app.use(pinia)

app.mount('#app')
