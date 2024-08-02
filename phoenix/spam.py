from telethon import events, errors
import phoenix.client
import asyncio

client = phoenix.client.client

# متغير عالمي لتخزين حالة النشر
is_publishing = False

@events.register(events.NewMessage(outgoing=True, pattern=r"\.نشر (\d+) (\d+) (.*)"))
async def publish(e):
    global is_publishing
    if is_publishing:
        return await e.edit("**النشر جاري بالفعل.**")

    try:
        count = int(e.pattern_match.group(1))
        delay = float(e.pattern_match.group(2))
        message = e.pattern_match.group(3)
    except ValueError:
        return await e.edit("**الرجاء إدخال الأرقام بشكل صحيح.**")

    is_publishing = True
    await e.delete()

    try:
        for i in range(count):
            await e.respond(message)
            await asyncio.sleep(delay)
    except errors.FloodWait as e:
        await e.respond(f"**انتظر {e.seconds} ثانية.**")
    except Exception as u:
        await e.respond(f"**حدث خطأ: {u}**")
    finally:
        is_publishing = False

@events.register(events.NewMessage(outgoing=True, pattern=r"\.إيقاف_النشر"))
async def stop_publishing(e):
    global is_publishing
    if is_publishing:
        is_publishing = False
        await e.edit("**تم إيقاف النشر.**")
    else:
        await e.edit("**لم يكن هناك نشر جاري.**")

# الكود الأصلي الخاص بالتكرار يبقى كما هو
@events.register(events.NewMessage(outgoing=True, pattern=".تكرار ?(.*)"))
async def delayspam(e):
    try:
        args = e.text.split(" ", 3)
        dark = float(args[1])
        count = int(args[2])
        msg = str(args[3])
    except BaseException:
        return await e.edit("**Ishlatish :** spam <each time> <count> <message>")
    await e.delete()
    try:
        for i in range(count):
            await e.respond(msg)
            await asyncio.sleep(dark)
    except Exception as u:
        await e.respond(f"**Hatolik :** `{u}`")
