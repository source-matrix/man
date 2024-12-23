import base64
import asyncio
from telethon import events
from asyncio import sleep
from telethon.sync import TelegramClient
from telethon import events
from telethon.events import NewMessage
from FINAL import client
import re

finalll = client.client
final = False
delete_previous_message = False

import asyncio
import logging
from telethon import TelegramClient, events
from telethon.errors import (
    FloodWaitError,
    ChatWriteForbiddenError,
    UserBannedInChannelError,
    PeerIdInvalidError,
)

logging.basicConfig(filename='publishing_errors.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

force_repeat_count = False 

async def reconnect(finalll, max_retries=5):
    retry_count = 0
    wait_time = 1
    while retry_count < max_retries:
        try:
            await finalll.connect()
            return True
        except (ConnectionError, ReadTimeoutError) as e:
            logging.error(f"Reconnection attempt {retry_count + 1} failed: {e}")
            await asyncio.sleep(wait_time)
            wait_time *= 2
            retry_count += 1
    return False

async def final_nshr(finalll, sleeptimet, chat, message):
    global final
    final = True
    last_sent_message = None
    while final:
        try:
            if message.media:
                new_sent_message = await finalll.send_file(chat, message.media, caption=message.text)
            else:
                new_sent_message = await finalll.send_message(chat, message.text)
            if last_sent_message and delete_previous_message:
                await last_sent_message.delete()
            last_sent_message = new_sent_message
            await asyncio.sleep(sleeptimet)
        except (ConnectionError, ReadTimeoutError):
            logging.error("Connection error occurred.")
            if not await reconnect(finalll):
                logging.error("Failed to reconnect after multiple attempts.")
                break
        except (FloodWaitError, ChatWriteForbiddenError, UserBannedInChannelError) as e:
            break
        except PeerIdInvalidError:
            break
        except Exception as e:
            logging.exception(f"An unexpected error occurred: {e}")

async def final_allnshr(finalll, sleeptimet, message):
    global final
    final = True
    last_sent_messages = {}
    while final:
        try:
            final_chats = await finalll.get_dialogs()
            for i, chat in enumerate(final_chats):
                if chat.is_group:
                    try:
                        if message.media:
                            new_sent_message = await finalll.send_file(chat.id, message.media, caption=message.text)
                        else:
                            new_sent_message = await finalll.send_message(chat.id, message.text)
                        if chat.id in last_sent_messages and delete_previous_message:
                            await last_sent_messages[chat.id].delete()
                        last_sent_messages[chat.id] = new_sent_message
                        await asyncio.sleep(1) 
                    except (FloodWaitError, ChatWriteForbiddenError, UserBannedInChannelError) as e:
                        pass
                    except PeerIdInvalidError:
                        pass
                    except Exception as e:
                        logging.exception(f"An unexpected error occurred in chat {chat.id}: {e}")
            await asyncio.sleep(sleeptimet)
        except (ConnectionError, ReadTimeoutError):
            logging.error("Connection error occurred.")
            if not await reconnect(finalll):
                logging.error("Failed to reconnect after multiple attempts.")
                break
        except Exception as e:
            logging.exception(f"Error in final_allnshr: {e}")

super_groups = ["super", "سوبر"]
async def final_supernshr(finalll, sleeptimet, message):
    global final
    final = True
    last_sent_messages = {}
    while final:
        try:
            final_chats = await finalll.get_dialogs()
            for i, chat in enumerate(final_chats):
                chat_title_lower = chat.title.lower()
                if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                    try:
                        if message.media:
                            new_sent_message = await finalll.send_file(chat.id, message.media, caption=message.text)
                        else:
                            new_sent_message = await finalll.send_message(chat.id, message.text)
                        if chat.id in last_sent_messages and delete_previous_message:
                            await last_sent_messages[chat.id].delete()
                        last_sent_messages[chat.id] = new_sent_message
                        await asyncio.sleep(1)
                    except (FloodWaitError, ChatWriteForbiddenError, UserBannedInChannelError) as e:
                        pass
                    except PeerIdInvalidError:
                        pass
                    except Exception as e:
                        logging.exception(f"An unexpected error occurred in chat {chat.id}: {e}")

            await asyncio.sleep(sleeptimet)
        except (ConnectionError, ReadTimeoutError):
            logging.error("Connection error occurred.")
            if not await reconnect(finalll):
                logging.error("Failed to reconnect after multiple attempts.")
                break
        except Exception as e:
            logging.exception(f"Error in final_supernshr: {e}")

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.تفعيل حذف النشر$"))
async def enable_delete_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return
    global delete_previous_message
    delete_previous_message = True
    await event.reply("✅ تم تفعيل حذف النشر السابق.")

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+)\s+(.+)$"))
async def final_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return
    await event.delete()
    
    seconds_str, chat_usernames_str = event.pattern_match.groups()  
    try:
        seconds = int(seconds_str)
    except ValueError:
        return await event.reply("  يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا  ")

    chat_usernames = re.split(r"\s*\|\s*", chat_usernames_str)  

    finalll = event.client
    global final
    final = True
    message = await event.get_reply_message()
    
    for chat_username in chat_usernames:
        try:
            chat = await finalll.get_entity(chat_username)
            await final_nshr(finalll, seconds, chat, message)
        except Exception as e:
            await event.reply(f"  لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}")



@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر_كروبات (\d+)$"))
async def final_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return
    await event.delete()
    
    seconds_str = event.pattern_match.group(1)
    try:
        sleeptimet = int(seconds_str)
    except ValueError:
        return await event.reply("  يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا  ")
    
    finalll = event.client
    global final
    final = True
    message = await event.get_reply_message()
    await final_allnshr(finalll, sleeptimet, message)


@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def final_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return
    await event.delete()
    
    seconds_str = event.pattern_match.group(1)
    try:
        sleeptimet = int(seconds_str)
    except ValueError:
        return await event.reply("  يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا  ")

    finalll = event.client
    global final
    final = True
    message = await event.get_reply_message()
    await final_supernshr(finalll, sleeptimet, message)

@finalll.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_final(event):
    if not isinstance(event, events.NewMessage.Event):
        return
    global final
    final = False
    await event.edit(" ︙ تم ايقاف النشر التلقائي بنجاح ✓  ")








    #======

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.(م11)$"))
async def final_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    if event.pattern_match.group(1) == "م11":
        final_commands = """**
  قـائمة اوامر النشر التلقائي للمجموعات

===== ===== =====

`.نشر` عدد الثواني معرف الكروب :
 - للنشر في المجموعة التي وضعت معرفها مع عدد الثواني

`.نشر_كروبات` عدد الثواني :
- للنشر في جميع المجموعات الموجوده في حسابك

`.سوبر` عدد الثواني :
- للنشر بكافة المجموعات السوبر التي منظم اليها

`.تناوب` عدد الثواني :
- للنشر في جميع المجموعات بالتناوب وحسب الوقت المحدد

`.خاص` :
- للنشر في جميع المحادثات الخاصة مرة واحدة فقط

`.نقط` عدد الثواني :
- للرد على نفس الرسالة ب (.) وحسب الوقت المحدد

`.بلش` عدد الثواني :
- لتكرار نفس الرسالة وحسب الوقت المحدد في انفس المحادثة فقط

`.سبام` :
- يرسل الجملة حرف بعد حرف الى ان تنتهي الجملة .

`.وسبام` :
- يرسل الجملة كلمة بعد كلمة

`.ايقاف النشر` :
- لأيقاف جميع انواع النشر اعلاه

`.تفعيل حذف النشر ` 
- يقوم بحذف الكليشة السابقة بعد ارسال الجديدة 

• مُـلاحظة : جميع الأوامر اعلاه تستخدم بالرد على الرسالة او الكليشة المُراد نشرها

• مُـلاحظة : جميع الأوامر اعلاه تستقبل صورة واحدة موصوفة بنص وليس اكثر من ذلك

======= =====

    **"""
        await event.respond(final_commands, parse_mode="md")

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.سبام$"))
async def spam_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    message = await event.get_reply_message()
    if not message or not message.text:
        return await event.reply("  يجب الرد على رسالة نصية لاستخدام هذا الأمر.")

    text = message.text
    for char in text:
        await event.respond(char)
        await asyncio.sleep(0.8)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.وسبام$"))
async def word_spam_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return
    await event.delete()
    message = await event.get_reply_message()
    if not message or not message.text:
        return await event.reply("  يجب الرد على رسالة نصية لاستخدام هذا الأمر.")

    words = message.text.split()
    for word in words:
        await event.respond(word)
        await asyncio.sleep(1)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.تناوب (\d+)$"))
async def rotate_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("  يجب الرد على رسالة لاستخدام هذا الأمر.")

    global final
    final = True
    chats = await finalll.get_dialogs()
    groups = [chat for chat in chats if chat.is_group]
    num_groups = len(groups)
    current_group_index = 0

    while final:
        try:
            if message.media:
                await finalll.send_file(groups[current_group_index].id, message.media, caption=message.text)
            else:
                await finalll.send_message(groups[current_group_index].id, message.text)
        except Exception as e:
            print(f"Error in sending message to chat {groups[current_group_index].id}: {e}")

        current_group_index = (current_group_index + 1) % num_groups
        await asyncio.sleep(seconds)
@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.خاص$"))
async def private_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    message = await event.get_reply_message()
    if not message:
        return await event.reply("  يجب الرد على رسالة لاستخدام هذا الأمر.")

    chats = await finalll.get_dialogs()
    private_chats = [chat for chat in chats if chat.is_user]

    for chat in private_chats:
        try:
            if message.media:
                await finalll.send_file(chat.id, message.media, caption=message.text)
            else:
                await finalll.send_message(chat.id, message.text)
        except Exception as e:
            print(f"Error in sending message to chat {chat.id}: {e}")

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.نقط (\d+)$"))
async def dot_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    reply_to_msg = await event.get_reply_message()
    if not reply_to_msg:
        return await event.reply("  يجب الرد على رسالة لاستخدام هذا الأمر.")

    global final
    final = True

    while final:
        await reply_to_msg.reply(".")
        await asyncio.sleep(seconds)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.بلش (\d+)$"))
async def repeat_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("  يجب الرد على رسالة لاستخدام هذا الأمر.")

    global final
    final = True

    while final:
        await message.respond(message)
        await asyncio.sleep(seconds)
