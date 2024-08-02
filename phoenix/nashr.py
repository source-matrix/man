from telethon import TelegramClient, events
import asyncio
import time

# افترض أن phoenix.client يقوم بإدارة تسجيل الدخول والتواصل مع السيرفر

# قاموس لتخزين حالة الإرسال
sending_status = {}

@client.on(events.NewMessage(pattern=r'\.نشر'))
async def start_sending(event):
    # تحليل الأوامر
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

    # حفظ حالة الإرسال
    chat_id = event.chat_id
    sending_status[chat_id] = {'count': count, 'message': message, 'stop': False}

    await event.reply('بدأ الإرسال')

    # وظيفة مساعدة لإرسال الرسالة
    async def send_messages():
        while sending_status[chat_t
