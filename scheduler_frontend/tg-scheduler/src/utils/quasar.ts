import { Notify } from 'quasar';

export function showNotify(params: any) {
    const blackColors = ['warning']

    if (!params.textColor) {
        params.textColor = blackColors.indexOf(params.color) !== -1 ? 'black' : ''
    }

    Notify.create(params)
}

export function showErrorNotify(message: string, timeout = 2500) {
    showNotify({
        message: message,
        color: 'negative',
        icon: 'report_problem',
        timeout: timeout
    })
}