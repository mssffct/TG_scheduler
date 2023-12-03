import { RouteRecordRawApp } from 'vue-router'

const routes: RouteRecordRawApp[] = [
  {
    path: '/',
    name: 'MainPage',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { name: 'EditPage', path: '/edit', component: () => import('pages/EditPage.vue') },
      { name: 'CreatePage', path: '/create', component: () => import('pages/CreatePage.vue') }
    ]
  },

  {
    path: '/login',
    name: 'LoginPage',
    component: () => import('pages/login/LoginPage.vue'),
    whiteList: true
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
