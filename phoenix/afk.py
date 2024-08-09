from telethon import events
from datetime import datetime
import asyncio
from telethon.tl.functions.users import GetFullUserRequest

afk_mode = False
custom_reply = "أنا لست موجودًا الآن، أرجوك اترك رسالتك وانتظر لحين عودتي."
reply_to_message = None

@events.register(events.NewMessage(outgoing=True, pattern=r'\.تشغيل الرد'))
async def enable_afk(event):
    global afk_mode
    afk_mode = True
    await event.edit("تم تشغيل الرد التلقائي.")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage(outgoing=True, pattern=r'\.تعطيل الرد'))
async def disable_afk(event):
    global afk_mode
    afk_mode = False
    await event.edit("تم تعطيل الرد التلقائي.")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage(outgoing=True, pattern=r'\.كليشة الرد'))
async def set_reply_template(event):
    global reply_to_message
    reply_to_message = await event.get_reply_message()
    if reply_to_message:
        await event.edit(f"تم تعيين كليشة الرد إلى الرسالة المحددة.")
    else:
        await event.edit("يرجى الرد على الرسالة التي تريد استخدامها ككليشة.")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage)
async def afk_handler(event):
    global afk_mode
    if not afk_mode and not await event.client.is_user_authorized():
        afk_mode = True

    if afk_mode and event.is_private:
        me = await event.client.get_me()
        sender = await event.get_sender()
        if sender.id != me.id and not sender.bot:
            if reply_to_message:
                await event.reply(reply_to_message)
            else:
                await event.reply(custom_reply)

async def check_connection_periodically():
    while True:
        if not await event.client.is_user_authorized():
            await asyncio.sleep(60)
        else:
            global afk_mode
            afk_mode = False
            break

@events.register(events.NewMessage)
async def start_background_tasks(event):
    if event.original_update.message.id == 1:
        asyncio.create_task(check_connection_periodically())

