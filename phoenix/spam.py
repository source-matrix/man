from telethon import events, errors
import phoenix.client
import asyncio

client = phoenix.client.client  # تأكد من تهيئة العميل بشكل صحيح

async def publish(event):
    # استخراج الوقت والعدد والرسالة من الأوامر
    args = event.message.raw_text.split()
    if len(args) < 4:
        await event.reply("الرجاء إدخال الأوامر بشكل صحيح: .نشر -الوقت -العدد- الرسالة")
        return

    time_interval = int(args[1])
    repeat_count = int(args[2])
    message = " ".join(args[3:])

    # الحصول على قائمة المجموعات التي يملكها المستخدم
    my_chats = await client.get_dialogs()
    groups = [chat for chat in my_chats if chat.is_group]

    # وظيفة مساعدة للنشر في مجموعة معينة
    async def publish_to_group(group):
        for _ in range(repeat_count):
            await client.send_message(group.entity, message)
            await asyncio.sleep(time_interval)

    # نشر الرسالة في كل مجموعة بالتوازي
    await asyncio.gather(*(publish_to_group(group) for group in groups))

async def repeat(event):
    # استخراج الوقت والعدد
    args = event.message.raw_text.split()
    if len(args) < 3:
        await event.reply("الرجاء إدخال الأوامر بشكل صحيح: .كرر -الوقت -العدد")
        return

    time_interval = int(args[1])
    repeat_count = int(args[2])

    # الحصول على الرسالة الأصلية
    original_message = event.message.reply_to_msg_id

    for _ in range(repeat_count):
        await client.forward_messages(event.chat_id, original_message)
        await asyncio.sleep(time_interval)

# معالجة الأوامر
@client.on(events.NewMessage(pattern=".نشر"))
async def handler(event):
    await publish(event)

@client.on(events.NewMessage(pattern=".كرر"))
async def handler(event):
    await repeat(event)

# تشغيل العميل
client.start()
client.run_until_disconnected()
