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
    try:
        args = e.text.split(" ", 4)  # نسمح بمسافة إضافية للعدد الثاني
        delay = int(args[1])
        count = int(args[2])
        message = str(args[3])
    except IndexError:
        await e.edit("**استخدام خاطئ:** .نشر <عدد الثواني> <عدد المرات> <الرسالة>")
        return

    dialogs = await client.get_dialogs()

    async def publish_to_group(dialog):
        for _ in range(count):
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

@events.register(events.NewMessage(outgoing=True, pattern=".ايقاف_الكل"))
async def stop_all_commands(e):
    global stop_spamming
    stop_spamming = True
    await e.edit("تم إيقاف جميع الأوامر")
@events.register(events.NewMessage(outgoing=True, pattern=".تناوب ?(.*)"))
async def publish_in_rotation(e):
    try:
        args = e.text.split(" ", 4)
        delay = int(args[1])
        count = int(args[2])
        message = str(args[3])
    except IndexError:
        await e.edit("**استخدام خاطئ:** .تناوب <عدد الثواني> <عدد المرات> <الرسالة>")
        return
    dialogs = await client.get_dialogs()
    groups = [dialog for dialog in dialogs if dialog.is_group]

    for _ in range(count):
      for group in groups:
        try:
            await client.send_message(group, message)
          
            await asyncio.sleep(delay)
        except Exception as ex:
            print(f"حدث خطأ أثناء الإرسال إلى المجموعة {group.title}: {ex}")
            
    await e.edit("تم الانتهاء من النشر بالتناوب")
