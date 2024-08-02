from telethon import events, errors
import phoenix.client
import asyncio

client = phoenix.client.client

# متغير عالمي لتخزين حالة النشر
is_darkspam = False

@events.register(events.NewMessage(outgoing=True, pattern=r".نشر ?(.*)"))
async def publish(e):
    global is_darkspam
    if is_darkspam:
        return await e.edit("**النشر جاري بالفعل.**")

    try:
        args = e.text.split(" ", 3)
        count = int(e.pattern_match.group(1))
        dark = float(e.pattern_match.group(2))
        msg = str(e.pattern_match.group(3))
    except ValueError:
        return await e.edit("**الرجاء إدخال الأرقام بشكل صحيح.**")

    is_darkspam = True
    await e.delete()

    try:
        for i in range(count):
            await e.respond(msg)
            await asyncio.sleep(dark)
    except errors.FloodWait as e:
        await e.respond(f"**انتظر {e.seconds} ثانية.**")
    except Exception as u:
        await e.respond(f"**حدث خطأ: {u}**")
    finally:
        is_darkspam = False

@events.register(events.NewMessage(outgoing=True, pattern=r"\.إيقاف_النشر"))
async def stop_darkspam(e):
    global is_darkspam
    if is_darkspam:
        is_darkspam = False
        await e.edit("**تم إيقاف النشر.**")
    else:
        await e.edit("**لم يكن هناك نشر جاري.**")

# الكود الأصلي الخاص بالتكرار يبقى كما هو
@events.register(events.NewMessage(outgoing=True, pattern=".تكرار ?(.*)"))
async def darkspam(e):
    try:
        args = e.text.split(" ", 3)
        dark = float(args[1])
        count = int(args[2])
        msg = str(args[3])
    except BaseException:
        return await e.edit("**هكذا :** الامر <الوقت> <العدد> <الرسالة>")
    await e.delete()
    try:
        for i in range(count):
            await e.respond(msg)
            await asyncio.sleep(dark)
    except Exception as u:
        await e.respond(f"**Hatolik :** `{u}`")
