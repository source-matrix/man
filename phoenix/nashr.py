from telethon import TelegramClient, events
import asyncio
import time
from client.py import api_id, api_hash


client = TelegramClient('session', api_id, api_hash)
is_running = False
message_to_send = None
interval = 10  # قيمة افتراضية للفترة الزمنية

@client.on(events.NewMessage(pattern='\.نشر (\d+)'))
async def start_sending(event):
    global is_running, message_to_send, interval
    if is_running:
        await event.reply('عملية النشر جارية بالفعل')
        return

    reply_to_msg = await event.get_reply_message()
    if not reply_to_msg:
        await event.reply('يجب الرد على رسالة تحتوي على الوسيط المراد نشره')
        return

    message_to_send = reply_to_msg
    interval = int(event.pattern_match.group(1))
    is_running = True
    await event.reply('بدء عملية النشر')
    asyncio.create_task(send_messages())

@client.on(events.NewMessage(pattern='\.ايقاف'))
async def stop_sending(event):
    global is_running
    if not is_running:
        await event.reply('لا توجد عملية نشر جارية')
        return

    is_running = False
    await event.reply('تم إيقاف عملية النشر')

async def send_messages():
    global is_running, message_to_send, interval
    while is_running:
        dialogs = await client.get_dialogs()
        for dialog in dialogs:
            if dialog.is_group:
                await client.send_message(dialog.entity, message_to_send, reply_to=message_to_send)
                await asyncio.sleep(interval)

client.start()
client.run_until_disconnected()
