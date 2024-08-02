from telethon import TelegramClient, events
import asyncio
import time

# افترض أن phoenix.client يقوم بإدارة تسجيل الدخول والتواصل مع السيرفر

sending_status = {}

@client.on(events.NewMessage(pattern=r'\.نشر'))
async def start_sending(event):
    args = event.message.raw_text.split()
    if len(args) < 3:
        await event.reply('الرجاء استخدام الأمر بشكل صحيح: .نشر -الوقت- العدد')
        return

    try:
        delay = int(args[1])
        count = int(args[2])
        reply_to = await event.get_reply_message()
        message = reply_to.message
    except ValueError:
        await event.reply('الوقت والعدد يجب أن يكونا أعداد صحيحة')
        return

    chat_id = event.chat_id
    sending_status[chat_id] = {'count': count, 'message': message, 'stop': False}

    await event.reply('بدأ الإرسال')
    asyncio.create_task(send_messages(chat_id, delay))

@client.on(events.NewMessage(pattern=r'\.ايقاف'))
async def stop_sending(event):
    chat_id = event.chat_id
    if chat_id in sending_status:
        sending_status[chat_id]['stop'] = True
        await event.reply('تم إيقاف الإرسال')

async def send_messages(chat_id, delay):
    while sending_status[chat_id]['count'] > 0 and not sending_status[chat_id]['stop']:
        await client.send_message(chat_id, sending_status[chat_id]['message'])
        sending_status[chat_id]['count'] -= 1
        await asyncio.sleep(delay)
