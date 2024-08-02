from telethon import TelegramClient, events
import asyncio
import time

# افترض أن phoenix.client يقوم بإدارة تسجيل الدخول والتواصل مع السيرفر

# قاموس لتخزين حالة الإرسال لكل محادثة
sending_status = {}

# تعريف عميل التليجرام (استبدل ببياناتك الخاصة)
client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(pattern=r'\.نشر'))
async def start_sending(event):
    """
    هذه الدالة تقوم ببدء عملية الإرسال المتكرر لرسالة معينة.

    :param event: حدث الرسالة الذي يحتوي على الأمر .نشر
    """

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

    # وظيفة مساعدة لإرسال الرسائل
    async def send_messages():
        while sending_status[chat_id]['count'] > 0 and not sending_status[chat_id]['stop']:
            await client.send_message(chat_id, message)
            sending_status[chat_id]['count'] -= 1
            await asyncio.sleep(delay)

    # تشغيل المهمة في الخلفية
    asyncio.create_task(send_messages())

@client.on(events.NewMessage(pattern=r'\.ايقاف'))
async def stop_sending(event):
    """
    هذه الدالة تقوم بإيقاف عملية الإرسال في محادثة معينة.

    :param event: حدث الرسالة الذي يحتوي على الأمر .ايقاف
    """

    chat_id = event.chat_id
    if chat_id in sending_status:
        sending_status[chat_id]['stop'] = True
        await event.reply('تم إيقاف الإرسال')
    else:
        await event.reply('لا يوجد عملية إرسال قيد التشغيل')

with client:
    client.loop.run_until_complete(client.start())
    print('بوت التلغرام يعمل الآن')
    client.run_forever()
