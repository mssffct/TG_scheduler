<template>
    <div class="q-pt-lx no-wrap">
        <div class="auth-box column justify-between items-center q-gutter-sm">
            <q-form @submit.prevent="loginAction" @reset="formResetAction" ref="authFormRef" 
                class="column q-gutter-y-md">
                <div v-if="login" class="form-box column items-center justify-between content-center q-gutter-sm">
                    <span class="text-h5 q-pb-lg">Log in</span>
                    <q-input class="input" outlined
                        label="login" v-model="authForm.username" input-class="auth-input">
                        <template v-slot:prepend>
                            <q-icon name="account_circle"></q-icon>
                        </template>
                    </q-input>
                    <q-input class="input" outlined
                        label="Password" v-model="authForm.password" input-class="auth-input" :type="inputPasswordType">
                        <template v-slot:prepend>
                            <q-icon name="password"></q-icon>
                        </template>
                        <template v-slot:append>
                            <q-btn @click="visibilityPassword = !visibilityPassword" round dense flat
                                :icon="showPasswordBtnIcon" />
                        </template>
                    </q-input>
                    <q-btn label="Register" @click="registerStart()" outline plain class="form-btn"/>
                    <q-btn label="Log in" @click="loginAction()" class="form-btn"></q-btn>
                </div>
                <div v-if="register" class="form-box column items-center justify-between content-center q-gutter-sm">
                    <span class="text-h5 q-pb-lg">Register</span>
                    <q-input class="input" outlined
                        label="login" v-model="registerForm.username" input-class="auth-input">
                        <template v-slot:prepend>
                            <q-icon name="account_circle"></q-icon>
                        </template>
                    </q-input>
                    <q-input class="input" outlined
                        label="Password" v-model="registerForm.password" input-class="auth-input" :type="inputPasswordType">
                        <template v-slot:prepend>
                            <q-icon name="password"></q-icon>
                        </template>
                        <template v-slot:append>
                            <q-btn @click="visibilityPassword = !visibilityPassword" round dense flat
                                :icon="showPasswordBtnIcon" />
                        </template>
                    </q-input>
                    <q-input class="input" outlined
                        label="Password again" v-model="registerForm.password2" input-class="auth-input" :type="inputPasswordType">
                        <template v-slot:prepend>
                            <q-icon name="password"></q-icon>
                        </template>
                        <template v-slot:append>
                            <q-btn @click="visibilityPassword = !visibilityPassword" round dense flat
                                :icon="showPasswordBtnIcon" />
                        </template>
                    </q-input>
                    <q-btn label="Back to login" @click="backToLogin()" class="form-btn" style="margin-top: 20px;"></q-btn>
                    <q-btn label="Register" @click="registerAction()" class="form-btn" style="margin-top: 20px;"></q-btn>
                </div>
                
            </q-form>
        </div>
    </div>
</template>

<script setup lang="ts">
import { reactive, ref, computed } from 'vue'
import { loginRequest, RegisterRequest } from 'src/api/user'
import { useQuasar } from 'quasar'
import { useUserStore } from 'src/stores/users'
import { showErrorNotify } from 'src/utils/quasar'
import { useRouter } from 'vue-router';

const userStore = useUserStore()
const $q = useQuasar()
const $router = useRouter()

const authFormRef = ref(null)
const authForm = reactive({
    username: '',
    password: ''
})

const registerForm = reactive({
    username: '',
    password: '',
    password2: ''
})

const login = ref(true)
const register = ref(false)

const redirect = () => {
    $router.push({path: '/'})
}

const errorAndReload = (error: string):void => {
    $q.notify({
        message: error,
        color: 'warning',
        timeout: 1500,
    })
    userStore.clearState()
    $router.push({name: 'LoginPage'})
}

const loginAction = () => {
    loginRequest(authForm).then(async (response) => {
        loginSuccess(response)
        redirect()
    }).catch(error => {       
        errorAndReload(error)
    })
}
const formResetAction = () => {
    authForm.username = ''
    authForm.password = ''
}

// Login
const loginSuccess = (response: {auth_token: string}) => {
    const token = response.auth_token
    if (!token) {
        showErrorNotify('Authorization error')
        return
    }
    userStore.setToken(token)
}

const visibilityPassword = ref(false)
const inputPasswordType = computed(() => visibilityPassword.value ? 'text' : 'password')
const showPasswordBtnIcon = computed(() => visibilityPassword.value ? 'visibility' : 'visibility_off')

const registerStart = ():void => {
    login.value = false
    register.value = true
}

const backToLogin = ():void => {
    login.value = true
    register.value = false
}

const registerAction = ():void => {
    RegisterRequest(registerForm).then(async(response) => {
        loginRequest(registerForm).then(async (response) => {
            loginSuccess(response)
            redirect()
        }).catch(error => {
            errorAndReload(error)
        })
    }).catch(error => {
        errorAndReload(error)
    })
}
</script>

<style lang="scss">
.auth-box {
    width: 100%;
    min-height: 60vh;
    padding-top: 15vh;

    .q-form {
        width: 30%
    }

    .form-box {
        height: 100%;
        .input {
            width: 100%;
        }
        .form-btn {
            width: 50%;
        }
        .code-input {
            width: 100%;
            font-size: 20px;
        }

    }
}
</style>