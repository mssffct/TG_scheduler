<template>
  <q-page class="row items-center justify-evenly">
    <div class="column content-center items-center q-gutter-sm">
      <div class="text-h5">Create Memo</div>

      <q-option-group
        v-model="memoForm.importance"
        :options="options"
        inline
      />
      <q-input v-model="memoForm.theme" type="text" label="Memo theme" outlined class="memo-form__item">
        <template v-slot:append>
          <q-icon name="edit"></q-icon>
        </template>
      </q-input>

      <q-input
        v-model="memoForm.description"
        filled
        autogrow
        outlined label="Memo description" class="memo-form__item">
        <template v-slot:append>
          <q-icon name="edit_note"></q-icon>
        </template>
      </q-input>

      <q-input filled v-model="memoForm.time_to_send" class="memo-form__item" label="Time to send">
        <template v-slot:prepend>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-date v-model="memoForm.time_to_send" mask="YYYY-MM-DD HH:mm">
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-date>
            </q-popup-proxy>
          </q-icon>
        </template>
        <template v-slot:append>
          <q-icon name="access_time" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-time v-model="memoForm.time_to_send" mask="YYYY-MM-DD HH:mm" format24h>
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-time>
            </q-popup-proxy>
          </q-icon>
        </template>
      </q-input>

      <q-btn label="Save Memo" @click="saveMemo()" class="memo-form__item" style="margin-top: 20px;"></q-btn>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { Memo, MEMO_IMPORTANCE } from 'src/models/memos'
import { reactive } from 'vue'
import { useQuasar } from 'quasar'
import { useRouter } from 'vue-router';
import { CreateRequest } from 'src/api/memo'

const $router = useRouter()
const $q = useQuasar()

const memoForm = reactive<Memo>({
    theme: '',
    description: '',
    importance: MEMO_IMPORTANCE.low,
    time_to_send: undefined
})

type ImportanceOptions = Array<{label: string, value: MEMO_IMPORTANCE, color?: string}>

const options: ImportanceOptions = [
    {label: 'Low', value: MEMO_IMPORTANCE.low, color: 'positive'},
    {label: 'Middle', value: MEMO_IMPORTANCE.middle, color: 'warning'},
    {label: 'High', value: MEMO_IMPORTANCE.high, color: 'negative'},
]

const saveMemo = () => {
  CreateRequest(memoForm).then(async (response) => {
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
        timeout: 1000,
    })
  })
}

</script>

<style lang="scss">
.memo-form__item {
  width: 30vw;
}
</style>
