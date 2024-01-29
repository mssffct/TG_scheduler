import request from 'src/utils/request'
import { UserModelRawF,UserRegisterModelRawF } from 'src/models/users'

// Login / Logout
export const loginRequest = (data: object) => {
    return request({
        url: '/auth/login',
        method: 'post',
        data,
        withoutError: true,
    })
}

export const logoutRequest = async () => {
    return request({
        url: '/auth/logout',
        method: 'post',
        withoutError: true,
    })
}

// Users
export const getUserInfo = () => {
    return new Promise((resolve, reject) => {
        request<UserModelRawF>({
            url: '/users/info',
            method: 'get'
        }).then(response => {
            resolve(response)
        }).catch(error => {
            reject(error)
        })
    })
}

export const RegisterRequest = (data: object) => {
    return new Promise((resolve, reject) => {
        request<UserRegisterModelRawF>({
            url: '/users/register',
            method: 'post',
            data
        }).then(response => {
            resolve(response)
        }).catch(error => {
            reject(error)
        })
    })
}

// Settings
export const getTelegramId = async () => {
    return request({
        url: '/settings/telegram_id',
        method: 'get',
    })
}

export const saveSettingsRequest = (data: object) => {
    return request({
        url: '/settings/save_settings',
        method: 'post',
        data,
    })
}
