import { useUserStore } from "src/stores/users"
import routes from "./routes"
import { getUserInfo } from "src/api/user"
import { LoadingBar } from "quasar"
import { Router } from "vue-router"
import { showErrorNotify } from 'src/utils/quasar'

const loginPageName = 'LoginPage'
const whiteList = routes.filter(route => route.whiteList).map(route => route.path)


export default function initNavigation(router: Router) {

    router.beforeEach(async (to, from, next) => {
        LoadingBar.start()

        const userStore = useUserStore()
        if (userStore.token) {
            if (to.name === loginPageName) {  // Login page with token (redirect)
                next({ name: '/' })
            }
            else {
                try {
                    const userInfo  = await getUserInfo()
                    userStore.setUserData(userInfo)
                    next()
                } catch (exc) {
                    console.error('Auth error')
                    console.error(exc)
                    userStore.clearState()
                    next({ name: loginPageName, query: { redirect: to.path } })
                }
            }
        } else {
            if (!whiteList.includes(to.path)) {
                next({ name: loginPageName, query: { redirect: to.path } })
            } else {
                next()
            }
        }
    })

    router.afterEach(async (to, from) => {
        LoadingBar.stop()
    })
}
