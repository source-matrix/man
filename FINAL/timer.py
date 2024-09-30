from telethon import events
from time import sleep
import asyncio
from telethon import events
import FINAL.client
client = FINAL.client.client

@events.register(events.NewMessage(outgoing=True, pattern="\.مؤقت"))
async def timer(event):
        msg=event.message.raw_text.split()
        t=int(msg[1])
        mins=0
        while t>0:
                secs=t
                if(secs>=60):
                        mins=secs//60
                        secs-=mins*60
                else: mins=0
                timer=f"{mins}:{secs}"
                await event.edit(timer)
                await asyncio.sleep(1)
                t-=1
        await event.edit("انتهى الوقت!!!")
        await asyncio.sleep(3)
        await event.delete()


@events.register(events.NewMessage(outgoing=True, pattern="\.تنازلي"))
async def numbers(event):
        msg=event.message.raw_text.split()
        t=int(msg[1])
        await event.delete()
        while t>0:
                sleep(1)
                await client.send_message(event.message.to_id,str(t))
                t-=1

@events.register(events.NewMessage(outgoing=True, pattern="\.اسم"))
async def setclock(event):
    from telethon.tl.functions.account import UpdateProfileRequest
    await event.edit('يتم تعيين الاسم الوقتي . . .')
    sleep(0.5)
    msg=event.message.raw_text.split()
    t=int(msg[1])
    t*=56
    while t>0:
            from datetime import datetime
            now = datetime.now()
            hour = now.hour
            minute = now.minute
            
            hour = hour % 12
            if hour == 0:
                hour = 12  
            time = f" {hour:02d}:{minute:02d} " 
            await client(UpdateProfileRequest(last_name=str(time)))
            await event.edit('تم تعيين الاسم الوقتي')
            sleep(0.5)
            await event.delete()
            await asyncio.sleep(56)
            t-=1
    await client(UpdateProfileRequest(last_name="الوقت تقريبي فقط !!"))




from telethon import events
from time import sleep

@events.register(events.NewMessage(outgoing=True, pattern=r'\.كشف المحذوفين'))
async def runsda(event):
    await event.edit("البحث عن...")
    sleep(1)
    await event.delete()
    messagelocation = event.to_id
    deletedid = []
    try:
        chatname = event.chat.title
        async for users in event.client.iter_participants(messagelocation):
            if users.deleted:
                deletedid.append(users.id)
        countdeletedid = len(deletedid)
        if countdeletedid == 1:
            await event.client.send_message(messagelocation, f"{countdeletedid} حساب محذوف تم العثور عليه \nاسم المجموعة: {chatname}")
        elif countdeletedid == 0:
            await event.client.send_message(messagelocation, f"لم يتم العثور على أي حسابات محذوفة\nاسم المجموعة: {chatname}")
        else:
            await event.client.send_message(messagelocation, f"{countdeletedid} حساب محذوف تم العثور عليهم \nاسم المجموعة: {chatname}")
    except:
        await event.client.send_message(messagelocation, "حدث خطأ ما")

@events.register(events.NewMessage(outgoing=True, pattern=r'\.اطرد المحذوفين'))
async def runrda(event):
    await event.edit("الرجاء الانتظار...")
    sleep(1)
    await event.delete()
    messagelocation = event.to_id
    deletedid = []
    try:
        chatname = event.chat.title
        async for users in event.client.iter_participants(messagelocation):
            if users.deleted:
                deletedid.append(users.id)
                await event.client.kick_participant(messagelocation, users.id)
        countdeletedid = len(deletedid)
        if countdeletedid == 1:
            await event.client.send_message(messagelocation, f"{countdeletedid} حساب محذوف تم حذفه من المجموعة\n اسم المجموعة:  {chatname}")
        elif countdeletedid == 0:
            await event.client.send_message(messagelocation, f"لم يتم العثور على أي حسابات محذوفة\nاسم المجموعة: {chatname}")
        else:
         await event.client.send_message(messagelocation, f"{countdeletedid} حساب محذوف تم حذفهم من المجموعة {chatname}")
    except:
        await event.client.send_message(messagelocation, "حدث خطأ ما")
 


from os import remove

auto_save_enabled = False

@events.register(events.NewMessage(outgoing=True, pattern=r'\.واو|\.حفظ الذاتية'))
async def rundrc(event):
    await event.delete()
    if event.pattern_match.group(0) == ".واو":
        try:
            getrestrictedcontent = await event.get_reply_message()
            downloadrestrictedcontent = await getrestrictedcontent.download_media()
            await event.client.send_file("me", downloadrestrictedcontent)
            remove(downloadrestrictedcontent)
        except:
            pass
    elif event.pattern_match.group(0) == ".حفظ الذاتية":
        global auto_save_enabled
        auto_save_enabled = not auto_save_enabled
        if auto_save_enabled:
            await event.edit("تم تفعيل حفظ الوسائط ذاتية التدمير تلقائيًا.")
        else:
            await event.edit("تم إيقاف حفظ الوسائط ذاتية التدمير تلقائيًا.")

@events.register(events.NewMessage)
async def auto_save_media(event):
    if auto_save_enabled:
        try:
            if event.media and event.media.ttl_seconds:  
                downloadrestrictedcontent = await event.download_media()
                await event.client.send_file("me", downloadrestrictedcontent)
                remove(downloadrestrictedcontent)
        except:
            pass




@events.register(events.NewMessage(outgoing=True, pattern=r'\.حفظ'))
async def runrts(event):
    await event.delete()
    try:
        foundrestrictedcontent = await event.get_reply_message()
        restricteddata = foundrestrictedcontent.message
        await event.client.send_message("me", restricteddata)
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.احداث'))
async def runrgm(event):
    await event.edit("جار التحويل اخر 10 احداث للرسائل المحفوظة...")
    sleep(1)
    await event.delete()
    try:
        targetgroup = event.to_id
        recoveredplace = "me"
        grouplog = await event.client.get_admin_log(targetgroup, edit=False, delete=True)
        for restore in grouplog:
            await event.client.send_message(recoveredplace, restore.original.action.message, silent=True)
    except:
        pass
        
@events.register(events.NewMessage(outgoing=True, pattern="\.بايو"))
async def setbioclock(event):
    from telethon.tl.functions.account import UpdateProfileRequest
    await event.edit('لحظة من فضلك . . .')
    sleep(0.5)
    msg=event.message.raw_text.split()
    t=int(msg[1])
    t*=56
    while t>0:
        from datetime import datetime
        now = datetime.now()
        hour = now.hour
        minute = now.minute
       
        hour = hour % 12
        if hour == 0:
            hour = 12  
        time = now.strftime(f"{hour:02d}:{minute:02d} | %A | %d | %B | %Y")  
        await client(UpdateProfileRequest(about=str(time)))
        await event.edit('تم وضع البايو الوقتي')
        sleep(0.5)
        await event.delete()
        await asyncio.sleep(56)
        t-=1
    await client(UpdateProfileRequest("Vaqt nisbiy tushuncha !!"))
