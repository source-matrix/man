import asyncio
from telethon import events
from phoenix.client import client

# متغير عالمي لتخزين معرف الرسالة الحالية
current_message_id = None

async def fff_vid(event):
    global current_message_id
    if event.message.text == '.فحص':
        if current_message_id:
            try:
                original_message = await event.client.get_messages(event.chat_id, ids=current_message_id)
                await event.reply(file=original_message.media)  # لإعادة إرسال الوسائط
            except Exception as e:
                await event.reply(f"حدث خطأ: {str(e)}")
            else:
                await event.reply(original_message.text)  # لإعادة إرسال النص
        else:
            await event.reply('لم يتم تحديد محتوى بعد.')
    elif event.message.text == '.اضف_فحص':
        current_message_id = event.message.id
        await event.reply('تم تحديد المحتوى بنجاح.')

# ... (باقي كود الملف)
