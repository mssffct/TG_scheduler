import request from 'src/utils/request'


export const CreateRequest = async (data: object) => {
    return request({
        url: '/memos/',
        method: 'post',
        data
    })
}

export const FetchRequest = async () => {
    return request({
        url: '/memos/',
        method: 'get'
    })
}

export const RetrieveRequest = async (memoId: string) => {
    return request({
        url: '/memos/${memoId}/',
        method: 'get'
    })
}

export const DeleteRequest = async (memoId: string) => {
    return request({
        url: '/memos/${memoId}/',
        method: 'delete'
    })
}

export const UpdateRequest = async (memoId: string, data: object) => {
    return request({
        url: '/memos/${memoId}/',
        method: 'patch',
        data
    })
}
