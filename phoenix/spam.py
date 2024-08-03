from telethon import events
import phoenix.client
import asyncio

client = phoenix.client.client  # تأكد من تهيئة العميل بشكل صحيح

@client.on(events.NewMessage(pattern=r"\.كرر (\d+)"))
async def repeat_message(event):
    reply_msg = event.message.reply_to_msg_id
    repeat_time = int(event.pattern_match.group(1))

    while True:
        await client.send_message(event.chat_id, reply_msg, reply_to=reply_msg)
        await asyncio.sleep(repeat_time)

        # تحقق من أمر التوقف
        if await client.wait_event(events.NewMessage(pattern=r"\.توقف", chats=event.chat_id)):
            await event.respond("تم إيقاف التكرار")
            break

# تشغيل العميل
client.start()
client.run_until_disconnected()
