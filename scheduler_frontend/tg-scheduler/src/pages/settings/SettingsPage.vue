<template>
    <q-page class="column items-center justify-center q-gutter-md">
        <q-input class="input form-item" outlined label="login" v-model="settingsForm.username" input-class="auth-input">
            <template v-slot:prepend>
                <q-icon name="account_circle"></q-icon>
            </template>
        </q-input>
        <q-input class="input form-item" outlined label="telegram id" v-model="settingsForm.telegram_id" input-class="auth-input">
            <template v-slot:prepend>
                <q-icon name="send"></q-icon>
            </template>
        </q-input>
        <q-btn label="Save" @click="saveSettings()" class="form-item" style="margin-top: 20px;"></q-btn>
    </q-page>
</template>

<script setup lang="ts">
import { reactive, onMounted } from 'vue'
import { getTelegramId, saveSettingsRequest } from 'src/api/user';
import { useQuasar } from 'quasar'
import { useRouter } from 'vue-router';
import { useUserStore } from 'src/stores/users';

const $router = useRouter()
const $q = useQuasar()
const store = useUserStore()

onMounted(async () => {
    settingsForm.username = store.userData?.username
    getTelegramId().then(async (response) => {
        settingsForm.telegram_id = response.telegram_id
    })
})

const settingsForm = reactive({
    username: '',
    telegram_id: null
})
const saveSettings = () => {
    saveSettingsRequest(settingsForm).then(async (response: string) => {
        $q.notify({
            message: response,
            color: 'green',
            timeout: 3000,
        })
        setTimeout(() => {
            $router.go(0)
        }, 3500);
    }).catch(error => {
        $q.notify({
            message: error,
            color: 'warning',
            timeout: 3000,
        })
    })
}
</script>

<style lang="scss">
.form-item {
    width: 30vw;
}
</style>
