<template>
  <q-page>
    <q-intersection v-for="memo in memosList" :key="memo" transition="flip-right" style="width:100%"
      class="q-gutter-sm q-mt-md">
      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar :color="getImportanceColor(memo.importance)">
            I
          </q-avatar>
        </q-item-section>
        <q-item-section>
          <q-item-label>Theme: {{ memo.theme }}</q-item-label>
        </q-item-section>
        <q-item-section>
          <q-item-label>Description: {{ memo.description }}</q-item-label>
        </q-item-section>
        <q-item-section>
          <q-icon v-if="memo.sent" name="mark_email_read" color="green" size="md"></q-icon>
          <q-icon v-if="!memo.sent" name="schedule_send" color="warning" size="md"></q-icon>
        </q-item-section>
        <q-item-section>Time: {{ friendlyDate(memo.time_to_send) }}</q-item-section>
        <q-item-section side style="width:100px">
          <div class="row items-center">
            <q-btn v-if="!memo.sent" icon="edit" flat round text-color="green" @click="updateMemoStart(memo)">
              <q-tooltip class="bg-grey-2 text-body2 text-grey-7">
                Update
              </q-tooltip>
            </q-btn>
            <q-btn icon="delete" flat round text-color="negative" @click="deleteMemo(memo.id)">
              <q-tooltip class="bg-grey-2 text-body2 text-grey-7">
                Delete
              </q-tooltip>
            </q-btn>
          </div>
        </q-item-section>
      </q-item>
    </q-intersection>

    <q-dialog v-model="memoUpdateDialog" persistent>
      <q-card>
        <q-card-section class="row content-center q-gutter-sm">
          <q-option-group v-model="updatedMemo.importance" :options="options" inline />

          <q-input v-model="updatedMemo.theme" type="text" label="Memo theme" outlined class="memo-form__item">
            <template v-slot:append>
              <q-icon name="edit"></q-icon>
            </template>
          </q-input>

          <q-input v-model="updatedMemo.description" filled autogrow outlined label="Memo description"
            class="memo-form__item">
            <template v-slot:append>
              <q-icon name="edit_note"></q-icon>
            </template>
          </q-input>

          <q-input filled v-model="updatedMemo.time_to_send" class="memo-form__item" label="Time to send">
            <template v-slot:prepend>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                  <q-date v-model="updatedMemo.time_to_send" mask="YYYY-MM-DD HH:mm">
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
                  <q-time v-model="updatedMemo.time_to_send" mask="YYYY-MM-DD HH:mm" format24h>
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </q-card-section>

        <q-card-actions align="center">
          <q-btn flat label="Cancel" color="primary" @click="closeUpdateDialog()" />
          <q-btn flat label="Save" color="primary" @click="updateMemo(updatedMemo)" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script setup lang="ts">
import { Memo, MEMO_IMPORTANCE } from 'src/models/memos'
import { ref, onMounted } from 'vue'
import { FetchRequest, DeleteRequest, UpdateRequest } from 'src/api/memo';
import { useQuasar } from 'quasar'
import { useRouter } from 'vue-router';

const $router = useRouter()
const $q = useQuasar()

onMounted(async () => {
  await FetchRequest().then(response => {
    memosList.value = response
  })
})

const memosList = ref()
const memoUpdateDialog = ref(false)
const updatedMemo = ref()

type ImportanceOptions = Array<{label: string, value: MEMO_IMPORTANCE, color?: string}>

const options: ImportanceOptions = [
    {label: 'Low', value: MEMO_IMPORTANCE.low, color: 'positive'},
    {label: 'Middle', value: MEMO_IMPORTANCE.middle, color: 'warning'},
    {label: 'High', value: MEMO_IMPORTANCE.high, color: 'negative'},
]

const colors = {
  [MEMO_IMPORTANCE.high]: 'red',
  [MEMO_IMPORTANCE.middle]: 'warning',
  [MEMO_IMPORTANCE.low]: 'green'
}
const getImportanceColor = (importance: MEMO_IMPORTANCE) => {
  return colors[importance]
}

const friendlyDate = (date: string) => {
  return date.slice(11, 19) + ' ' + date.slice(8, 10) + '-' + date.slice(5, 7) + '-' + date.slice(0, 4)
}

const successAndReload = (message: string) => {
  $q.notify({
    message: message,
    color: 'green',
    timeout: 3000,
  })
  setTimeout(() => {
    $router.go(0)
  }, 3500);
}

const errorNotify = (message: string) => {
  $q.notify({
    message: message,
    color: 'warning',
    timeout: 3000,
  })
}

const deleteMemo = async (memo_id: number) => {
  DeleteRequest({ id: memo_id }).then(async (response: string) => {
    successAndReload(response)
  }).catch(error => {
    errorNotify(error)
  })
}
const updateMemoStart = (memo: Memo) => {
  memoUpdateDialog.value = true
  updatedMemo.value = memo
}

const updateMemo = async (memo: Memo) => {
  UpdateRequest(memo).then(async (response: string) => {
    successAndReload(response)
  }).catch(error => {
    errorNotify(error)
  })
}

const closeUpdateDialog = () => {
  memoUpdateDialog.value = false
  updatedMemo.value = undefined
}
</script>

<style lang="scss">
.memo-form__item {
  width: 100%;
}
</style>

