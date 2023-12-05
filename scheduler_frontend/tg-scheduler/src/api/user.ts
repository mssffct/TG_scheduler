import request from 'src/utils/request'
import { UserModelRawF,UserRegisterModelRawF } from 'src/models/users'

export const loginRequest = (data: object) => {
    return request({
        url: '/auth/token/login',
        method: 'post',
        data,
        withoutError: true,
    })
}

export const getUserInfo = () => {
    return new Promise((resolve, reject) => {
        request<UserModelRawF>({
            url: '/auth/user/info',
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
            url: '/auth/user/register',
            method: 'post',
            data
        }).then(response => {
            resolve(response)
        }).catch(error => {
            reject(error)
        })
    })
}

export const logoutRequest = async () => {
    return request({
        url: '/auth/token/logout',
        method: 'post',
        withoutError: true,
    })
}

export const getTelegramId = async () => {
    return request({
        url: '/auth/settings/telegram_id',
        method: 'get',
    })
}

export const saveSettingsRequest = (data: object) => {
    return request({
        url: '/auth/settings/save_settings',
        method: 'post',
        data,
    })
}
