from telethon import events
import phoenix.client
import asyncio
import time

client = phoenix.client.client  # تأكد من تهيئة العميل بشكل صحيح ببيانات تسجيل الدخول

async def get_group_ids():
    dialogs = await client.get_dialogs()
    group_ids = [dialog.entity.id for dialog in dialogs if dialog.is_group]
    return group_ids

async def send_to_all_groups(message, delay, count):
    group_ids = await get_group_ids()

    for _ in range(count):
        for group_id in group_ids:
            await client.send_message(group_id, message)
        await asyncio.sleep(delay)
@client.on(events.NewMessage(pattern=r"\.نشر(\d+) -عدد (\d+)"))
async def handler(event):
    delay = int(event.pattern_match.group(1))
    count = int(event.pattern_match.group(2))
    await event.respond("بدء النشر...")
    asyncio.create_task(send_to_all_groups(event.message.message, delay, count))

@client.on(events.NewMessage(pattern=r"\.ايقاف_النشر"))
async def stop_handler(event):
    # هنا يمكنك إضافة منطق لإيقاف المهام المتزامنة
    print("تم إيقاف النشر")

client.start()
client.run_until_disconnected()
