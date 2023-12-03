import { defineStore } from 'pinia';

export interface UserData {
    username?: string,
    tg_settings_presence?: boolean,
}

interface State {
    token: null | string,
    userData?: UserData,
}

interface Actions {
    setToken(token: string): void
    setUserData(data: any): void
    clearState(): void
}

export const useUserStore = defineStore<string, State, {}, Actions>('user', {
    state: () => {
        return {
            token: null,
            userData: undefined,
        }
    },
    getters: {
    },

    actions: {
        setToken(token: string) {
            this.token = token
        },
        setUserData(data: any) {
            this.userData = data
        },
        clearState() {
            this.$patch(state => {
                state.token = null,
                state.userData = undefined
            })
        },
        
    }
});