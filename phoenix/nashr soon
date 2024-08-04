import asyncio
from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon import events

async def nashr(client, message):
    """
    توجيه رسالة إلى جميع المحادثات الخاصة.

    Args:
        client: كائن العميل الخاص بـ Telethon.
        message: النص الذي سيتم توجيهه.
    """

    # الحصول على قائمة بجميع المحادثات الخاصة
    result = await client(GetDialogsRequest(
        limit=None,
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        exclude_pinned=True,
    ))
    dialogs = result.dialogs

    # إرسال الرسالة إلى كل محادثة خاصة مرة واحدة
    for dialog in dialogs:
        if dialog.is_group:
            continue  # تجاهل المجموعات
        try:
            await client.send_message(dialog.id, message)
        except Exception as e:
            print(f"فشل إرسال الرسالة إلى {dialog.name}: {e}")

    # إرسال رسالة تأكيد للمستخدم
    await client.send_message(message.chat_id, f"تم توجيه الرسالة إلى {len(dialogs)} مستخدم.")

# معالجة الأمر .توجيه
@client.on(events.NewMessage(pattern=r"\.توجيه (.*)"))
async def handler(event):
    message = event.pattern_match.group(1)
    await nashr(client, message)

# معالجة الأمر .مساعدة
@client.on(events.NewMessage(pattern=r"\.مساعدة"))
async def help_handler(event):
    await event.reply("قائمة الأوامر:\n.توجيه (الرسالة): لتوجيه رسالة إلى جميع المحادثات الخاصة")
