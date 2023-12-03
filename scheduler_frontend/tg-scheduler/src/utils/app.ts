import { useUserStore } from 'src/stores/users';
import { logoutRequest } from 'src/api/user';


export async function logout() {
    const userStore = useUserStore()

    try {
        await logoutRequest()
    } finally {
        userStore.clearState()
    }
}