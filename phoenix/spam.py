from telethon import events
import phoenix.client
import asyncio
client = phoenix.client.client

spamming = False

@events.register(events.NewMessage(outgoing=True, pattern=".كرر ?(.*)"))
async def delayspam(e):
    global spamming
    try:
        args = e.text.split(" ", 3)
        dark = float(args[1])
        count = int(args[2])
        msg = str(args[3])
    except BaseException:
        return await e.edit("**هكذا :** الامر <الوقت> <العدد> <الرسالة>")
    await e.delete()
    try:
        spamming = True
        for i in range(count):
            if not spamming:
                break
            await e.respond(msg)
            await asyncio.sleep(dark)
        spamming = False
    except Exception as u:
        await e.respond(f"**خطا :** `{u}`")

@events.register(events.NewMessage(outgoing=True, pattern=".ايقاف_التكرار"))
async def stopspam(e):
    global spamming
    spamming = False
    await e.respond("لقد توقف.")
