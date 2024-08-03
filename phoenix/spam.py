from telethon import events, errors
import asyncio
import time
import random

# ... استيراد أي مكتبات أخرى تحتاجها

# وظيفة لإرسال رسالة إلى مجموعة معينة
async def send_message_to_group(client, group_entity, message):
    try:
        await client.send_message(group_entity, message)
    except errors.FloodWait as e:
        await asyncio.sleep(e.seconds)
        await send_message_to_group(client, group_entity, message)
    except Exception as e:
        print(f"Error sending message to {group_entity.title}: {str(e)}")

# وظيفة لإرسال رسائل جماعية
async def spam_groups(client, groups, message, delay):
    for group in groups:
        try:
            await send_message_to_group(client, group, message)
            await asyncio.sleep(delay)
        except Exception as e:
            print(f"Error processing group {group.title}: {str(e)}")

# وظيفة للحصول على قائمة المجموعات
async def get_groups(client):
    dialogs = await client.get_dialogs()
    return [dialog.entity for dialog in dialogs if dialog.is_group]

# معالج الأحداث لبدء عملية الإرسال
@events.register(events.NewMessage(outgoing=True, pattern=r".نشر (\d+) (.*)"))
async def delayspam(event):
    try:
        delay_time = int(event.pattern_match.group(1))
        message = event.pattern_match.group(2)
        groups = await get_groups(client)

        # يمكنك هنا إضافة منطق لتحديد مجموعات محددة لإرسال الرسائل إليها
        # مثلاً:
        # groups = [group for group in groups if "اسم المجموعة" in group.title]

        await event.edit("بدء عملية الإرسال...")
        await spam_groups(client, groups, message, delay_time)
        await event.edit("تم الانتهاء من عملية الإرسال")
    except Exception as e:
        await event.edit(f"حدث خطأ: {str(e)}")

# ... باقي معالجات الأحداث
