export enum MEMO_IMPORTANCE {
    high = 'high',
    middle = 'middle',
    low = 'low'
}

export enum MEMO_FIELDS {
    importance = 'importance',
    theme = 'theme',
    description = 'description',
    time_to_send = 'time_to_send'
}


export interface Memo {
    [MEMO_FIELDS.importance]: MEMO_IMPORTANCE;
    [MEMO_FIELDS.theme]: string;
    [MEMO_FIELDS.description]?: string;
    [MEMO_FIELDS.time_to_send]?: number | undefined;
}