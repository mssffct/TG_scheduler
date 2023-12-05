<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          TG Sheduler
        </q-toolbar-title>
        {{ userName }}
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      :width="65"
    >
      <div class="column content-center justify-between q-pt-xl" style="height: 100%; width:100%;">
        <div class="column content-center">
          <q-btn size='sm' icon="add_circle" flat label="Create" stack no-caps @click="clickTab('/')" />
          <q-btn size='sm' icon="edit_note" flat label="Edit" stack no-caps @click="clickTab('/edit')" />
          <q-btn size='sm' icon="settings" flat label="Settings" stack no-caps @click="clickTab('/settings')" />
        </div>
        <q-btn size='sm' icon="logout" flat label="Logout" stack no-caps @click="logoutAction" />
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { logout } from 'src/utils/app';
import { useRouter } from 'vue-router';
import { useUserStore } from 'src/stores/users';

const userStore = useUserStore()
const userName = userStore.$state.userData?.username
const leftDrawerOpen = ref(false)

function toggleLeftDrawer () {
  leftDrawerOpen.value = !leftDrawerOpen.value
}

const $router = useRouter()
const logoutAction = async () => {
    await logout()
    $router.go(0)
}

const clickTab = (link: string) => {
    $router.push({path: link})
}
</script>
