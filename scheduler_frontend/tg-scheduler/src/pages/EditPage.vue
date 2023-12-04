<template>
  <q-page>
    <q-intersection v-for="memo in memosList" :key="memo" transition="flip-right" style="width:100%" class="q-gutter-sm q-mt-md">
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
        <q-item-section>Time: {{ friendlyDate(memo.time_to_send) }}</q-item-section>
        <q-item-section side style="width:100px">
          <q-btn icon="delete" flat round text-color="negative" @click="deleteMemo(memo.id)">
            <q-tooltip class="bg-grey-2 text-body2 text-grey-7">
                Delete
            </q-tooltip>
          </q-btn>
        </q-item-section>
      </q-item>
    </q-intersection>
  </q-page>
</template>

<script setup lang="ts">
import { Memo, MEMO_IMPORTANCE } from 'src/models/memos'
import { ref, onMounted } from 'vue'
import { FetchRequest, DeleteRequest } from 'src/api/memo';
import { useQuasar } from 'quasar'
import { useRouter } from 'vue-router';

const $router = useRouter()
const $q = useQuasar()

onMounted(async () => {
    await FetchRequest().then(response => {
      console.log(response)
      memosList.value = response
    })
})

const memosList = ref()

const colors = {
  [MEMO_IMPORTANCE.high]: 'red',
  [MEMO_IMPORTANCE.middle]: 'warning',
  [MEMO_IMPORTANCE.low]: 'green'
}
const getImportanceColor = (importance: MEMO_IMPORTANCE) => {
  return colors[importance]
}

const friendlyDate = (date: string) => {
  return date.slice(11,19) +' '+ date.slice(8,10) +'-'+ date.slice(5,7) +'-'+ date.slice(0,4)
}

const deleteMemo = async (memo_id: number) => {
  DeleteRequest({id: memo_id}).then(async (response: string) => {
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

