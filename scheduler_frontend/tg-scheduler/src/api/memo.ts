import request from 'src/utils/request'


export const CreateRequest = async (data: object) => {
    return request({
        url: '/memos/create_memo',
        method: 'post',
        data
    })
}

export const FetchRequest = async () => {
    return request({
        url: '/memos',
        method: 'get'
    })
}

export const DeleteRequest = async (data: object) => {
    return request({
        url: '/memos/delete_memo',
        method: 'delete',
        data
    })
}