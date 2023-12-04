import { store } from 'quasar/wrappers'
import { createPinia } from 'pinia'
import { Router } from 'vue-router'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'


declare module 'pinia' {
  export interface PiniaCustomProperties {
      readonly user: string,
      readonly router: Router;
  }
}

export default store((/* { ssrContext } */) => {
  const pinia = createPinia()

  // Плагины
  pinia.use(piniaPluginPersistedstate)  // https://prazdevs.github.io/pinia-plugin-persistedstate/

  return pinia
})