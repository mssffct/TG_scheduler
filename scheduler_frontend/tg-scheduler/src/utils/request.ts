import axios, { AxiosInterceptorManager, InternalAxiosRequestConfig } from 'axios'
import { showErrorNotify } from './quasar'
import { useUserStore } from 'src/stores/users'
import { LoadingBar } from 'quasar'

// AxiosResponse
interface AppResponse {
    config: RequestConfig,
    status: number;
    data: any,
    request: RequestConfig
}

// AxiosInstance
interface AppAxiosInstance {
    <R = any>(config: RequestConfig): Promise<R>

    interceptors: {
        request: AxiosInterceptorManager<RequestConfig>;
        response: AxiosInterceptorManager<AppResponse>;
    };
}

// InternalAxiosRequestConfig
interface RequestConfig extends Omit<InternalAxiosRequestConfig, 'headers'> {
    url: string;
    method: 'get' | 'post' | 'put' | 'delete' | 'patch';
    headers?: object,
    withoutError?: Boolean,  // don't show error
    fullResponse?: Boolean,  // return response (default - response.data)
    formData?: Boolean,  // as Form data
    loading?: Boolean, // LoadingBar
}

// Стандартные настройки
const config: Omit<RequestConfig, "url" | "method"> = {
    baseURL: process.env.API_URL + '/api',
    timeout: 60000,
    withoutError: false,
    fullResponse: false,
    formData: false,
    loading: false,
    headers: {},
}

const service = axios.create(config) as AppAxiosInstance

service.interceptors.request.use(
    config => {
        if (config.loading) LoadingBar.start()

        // end slash
        const url = config.url
        config.url = url.endsWith('/') ? url : url + '/'

        // Content-Type
        const contentType = config.formData ? 'multipart/form-data' : 'application/json;charset=UTF-8'
        config.headers!['Content-Type'] = contentType

        // Auth token
        const userStore = useUserStore()
        if (userStore.token) { config.headers!['Authorization'] = 'Token ' + userStore.token }


        return config
    },
    error => {
        return Promise.reject(error)
    }
)

service.interceptors.response.use(
    response => {
        if (response?.config.loading) LoadingBar.stop()

        if (response.config.fullResponse) return response

        return response.data
    },
    error => {
        if (error.config?.loading) LoadingBar.stop()
        // Get error message from ErrorREsponse
        if (error?.response?.status == 503) {
            const resp = error?.response?.data?.description ? error?.response?.data?.description : error
            return Promise.reject(resp)
        }

        if (!error.config?.withoutError) {
            showErrorNotify('Error')
        }

        return Promise.reject(error)
    }
)

export default service