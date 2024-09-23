from telethon import events
import FINAL.client
import asyncio
from telethon.tl.types import Message
import re

client = FINAL.client.client


@events.register(events.NewMessage(outgoing=True, pattern='\.يوت (.+)'))
async def tconv(event):
    chat = await event.get_chat()
    sentence_to_summarize = event.pattern_match.group(1)

    if sentence_to_summarize.startswith("."):
        sentence_to_summarize = sentence_to_summarize[1:].strip()

    sentence_to_summarize = "يوت " + sentence_to_summarize

    await event.edit("انتظر...")

    x = await client.send_message('@x_h_9bot', sentence_to_summarize)

    async with client.conversation('@x_h_9bot') as conv:
        audio_clip = None
        timeout = 30
        start_time = asyncio.get_event_loop().time()

        while asyncio.get_event_loop().time() - start_time < timeout:
            response = await conv.get_response(x.id)
            await client.send_read_acknowledge(conv.chat_id)

            if response.audio:
                audio_clip = response
                break

        if audio_clip:
            new_message = Message(
                id=0,
                peer_id=chat,
                message="",
                media=audio_clip.media,
                entities=None,
                reply_markup=None,
                ttl_period=None
            )

            await client.send_message(chat, new_message, silent=True)
            await event.delete()
        else:
            await event.edit("المحتوى غير موجود")
#اخمطة وكول اني مطور هههههههههههههههههههههههههههههههههههههههههههههههه



@events.register(events.NewMessage(outgoing=True, pattern='\.سوال (.*)'))
async def tco(event):
    chat = await event.get_chat()
    question = event.pattern_match.group(1)  # استخراج السؤال من الأمر
    await event.edit("انتظر...")

    # إزالة أمر /start
    # await client.send_message('@SAMI_PAI_BOT', '/start') 

    async with client.conversation('@SAMI_PAI_BOT') as conv:
        await conv.send_message(question)  # إرسال السؤال مباشرةً إلى البوت

        # انتظار 3 ثواني قبل إعادة التوجيه للسماح للبوت بالكتابة
        await asyncio.sleep(7)

        xx = await conv.get_response()  # الحصول على رد البوت

        # إزالة الروابط من النص
        text_without_links = re.sub(r'http\S+', '', xx.text)

        await client.send_read_acknowledge(conv.chat_id)
        await client.send_message(chat, text_without_links)
        await event.message.delete()
