from telethon import events
import phoenix.client
import asyncio

client = phoenix.client.client

# متغير عالمي لتخزين حالة التكرار
repeating = False
# متغير عالمي لتخزين الرسالة التي سيتم تكرارها
repeat_message = ""

@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    global repeating, repeat_message
    if event.message.startswith(".كرر"):
        # استخراج وقت التكرار من الرسالة
        try:
            _, time_str = event.message.split()
            time_to_sleep = float(time_str)
        except ValueError:
            await event.reply("أدخل الوقت بشكل صحيح (رقم)")
            return
        # حفظ الرسالة التي تلي أمر التكرار
        repeat_message = event.message.replace(".كرر " + time_str, "")
        # بدء التكرار
        repeating = True
        await event.reply("بدء التكرار")
        while repeating:
            await event.respond(repeat_message)
            await asyncio.sleep(time_to_sleep)
    elif event.message == ".توقف":
        # إيقاف التكرار
        repeating = False
        await event.reply("تم إيقاف التكرار")

# تشغيل العميل
client.start()
client.run_until_disconnected()
