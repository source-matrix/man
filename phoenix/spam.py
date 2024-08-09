from telethon import events
import phoenix.client
import asyncio

client = phoenix.client.client

saved_messages = {
    ".كرر": None,
    ".نشر": None,
    ".تناوب": None
}

@events.register(events.NewMessage(outgoing=True, pattern=".كرر"))
async def delayspam(e):
    try:
        args = e.text.split(" ", 3)
        dark = float(args[1])
        count = int(args[2])
        reply_to_msg = await e.client.get_messages(e.chat_id, ids=e.reply_to_msg_id)
        msg = reply_to_msg.message
        saved_messages[".كرر"] = msg
        for i in range(count):
            if saved_messages[".كرر"] is None: # تحقق قبل كل تكرار
                break
            await e.respond(msg)
            await asyncio.sleep(dark)
    except Exception as u:
        await e.respond(f"**خطا :** `{u}`")

@events.register(events.NewMessage(outgoing=True, pattern=".نشر"))
async def publish_to_groups(e):
    try:
        args = e.text.split(" ", 4)
        delay = int(args[1])
        count = int(args[2])
        reply_to_msg = await e.client.get_messages(e.chat_id, ids=e.reply_to_msg_id)
        message = reply_to_msg.message
        saved_messages[".نشر"] = message
        dialogs = await client.get_dialogs()
        async def publish_to_group(dialog):
            for _ in range(count):
                if saved_messages[".نشر"] is None:
                    break
                await asyncio.sleep(delay)
                try:
                    await client.send_message(dialog, message)
                except Exception as ex:
                    print(f"حدث خطأ أثناء الإرسال إلى المجموعة {dialog.title}: {ex}")
        tasks = []
        for dialog in dialogs:
            if dialog.is_group:
                task = asyncio.create_task(publish_to_group(dialog))
                tasks.append(task)
        await asyncio.gather(*tasks)
        await e.edit("تم الانتهاء من النشر")
    except IndexError:
        await e.edit("**استخدام خاطئ:** .نشر <عدد الثواني> <عدد المرات> (يجب الرد على رسالة أولاً)")

@events.register(events.NewMessage(outgoing=True, pattern=".تناوب"))
async def publish_in_rotation(e):
    try:
        args = e.text.split(" ", 4)
        delay = int(args[1])
        count = int(args[2])
        reply_to_msg = await e.client.get_messages(e.chat_id, ids=e.reply_to_msg_id)
        message = reply_to_msg.message
        saved_messages[".تناوب"] = message
        dialogs = await client.get_dialogs()
        groups = [dialog for dialog in dialogs if dialog.is_group]
        for _ in range(count):
            for group in groups:
                if saved_messages[".تناوب"] is None:
                    break
                try:
                    await client.send_message(group, message)
                    await asyncio.sleep(delay)
                except Exception as ex:
                    print(f"حدث خطأ أثناء الإرسال إلى المجموعة {group.title}: {ex}")
        await e.edit("تم الانتهاء من النشر بالتناوب")
    except IndexError:
        await e.edit("**استخدام خاطئ:** .تناوب <عدد الثواني> <عدد المرات> (يجب الرد على رسالة أولاً)")

@events.register(events.NewMessage(outgoing=True, pattern=".ايقاف (.+)"))
async def stop_command(e):
    command_to_stop = e.pattern_match.group(1).strip()
    if command_to_stop in saved_messages:
        saved_messages[command_to_stop] = None
        await e.edit(f"تم إيقاف أمر {command_to_stop}")
    else:
        await e.edit("الأمر غير موجود أو غير نشط حاليًا")
