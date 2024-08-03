from telethon import events
import phoenix.client
import asyncio

client = phoenix.client.client

# قاموس لتخزين حالة التكرار لكل مستخدم
spamming_users = {}

@events.register(events.NewMessage(outgoing=True, pattern=".كرر ?(.*)"))
async def delayspam(e):
    global spamming_users
    try:
        args = e.text.split(" ", 3)
        dark = float(args[1])
        count = int(args[2])
        msg = str(args[3])
    except BaseException:
        return await e.edit("**هكذا :** الامر <الوقت> <العدد> <الرسالة>")
    await e.delete()
    try:
        # تخزين حالة التكرار للمستخدم الحالي
        spamming_users[e.sender_id] = True
        for i in range(count):
            if not spamming_users.get(e.sender_id, False):
                break
            await e.respond(msg)
            await asyncio.sleep(dark)
        # حذف حالة التكرار بعد الانتهاء
        del spamming_users[e.sender_id]
    except Exception as u:
        await e.respond(f"**خطا :** `{u}`")

@events.register(events.NewMessage(outgoing=True, pattern=".ايقاف_التكرار"))
async def stopspam(e):
    global spamming_users
    # إيقاف التكرار للمستخدم الحالي
    spamming_users[e.sender_id] = False
    await e.respond("لقد توقف.")
