import { RouteRecordRawApp } from 'vue-router'

const routes: RouteRecordRawApp[] = [
  {
    path: '/login',
    name: 'LoginPage',
    component: () => import('pages/login/LoginPage.vue'),
    whiteList: true
  },
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { name: 'CreatePage', path: '', component: () => import('pages/CreatePage.vue') }
    ]
  },
  {
    path: '/edit',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { name: 'EditPage', path: '', component: () => import('pages/EditPage.vue') }
    ]
  },
  {
    path: '/settings',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { name: 'SettingsPage', path: '', component: () => import('pages/settings/SettingsPage.vue') }
    ]
  },
  // Always leave this as last one,
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
