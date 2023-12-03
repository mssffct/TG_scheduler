export enum USER_FIELDS {
    id = 'id',
    username = 'username',
    tg_settings_presence = 'tg_settings_presence'
}

export enum USER_REGISTER_FIELDS {
    username = 'username',
    password = 'password',
    password2 = 'password2'
}

export type UserModelRawF = {
    [USER_FIELDS.id]: number,
    [USER_FIELDS.username]: string,
    [USER_FIELDS.tg_settings_presence]: boolean
}

export type UserRegisterModelRawF = {
    [USER_REGISTER_FIELDS.username]: string,
    [USER_REGISTER_FIELDS.password]: string,
    [USER_REGISTER_FIELDS.password2]: string,
}