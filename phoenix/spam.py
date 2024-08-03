from telethon import events
import phoenix.client
import asyncio

client = phoenix.client.client
stop_spamming = False

@events.register(events.NewMessage(outgoing=True, pattern=".تكرار ?(.*)"))
async def delayspam(e):
    try:
        args = e.text.split(" ", 3)
        dark = float(args[1])
        count = int(args[2])
        msg = str(args[3])
    except BaseException:
        return await e.edit("**هكذا يستخدم  :** الامر <الوقت> <العدد> <الرسالة>")
    await e.delete()
    try:
        for i in range(count):
            await e.respond(msg)
            await asyncio.sleep(dark)
    except Exception as u:
        await e.respond(f"**خطا :** `{u}`")

@events.register(events.NewMessage(outgoing=True, pattern=".نشر ?(.*)"))
async def publish_to_groups(e):
    global stop_spamming
    stop_spamming = False

    try:
        args = e.text.split(" ", 3)
        delay = int(args[1])
        message = str(args[2])
    except IndexError:
        await e.edit("**استخدام خاطئ:** .نشر <عدد الثواني> <الرسالة>")
        return

    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_group:
            await e.edit(f"بدء النشر في المجموعة: {dialog.title}")
            while not stop_spamming:
                await client.send_message(dialog, message)
                await asyncio.sleep(delay)
    await e.edit("تم الانتهاء من النشر")

@events.register(events.NewMessage(outgoing=True, pattern=".ايقاف"))
async def stop_spamming_command(e):
    global stop_spamming
    stop_spamming = True
    await e.edit("تم إيقاف النشر")
