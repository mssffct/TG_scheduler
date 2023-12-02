from telethon import events

from config import bot


@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event) -> None:
    chat_id = event.peer_id

    async with bot.conversation(chat_id) as conv:
        await conv.send_message(
            f'Hi! Here is your id: \n\n<strong>{chat_id}</strong>\n\nCopy it and paste to your TG Scheduler settings',
            parse_mode="html"
        )
