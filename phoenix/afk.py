from telethon import events
from datetime import datetime
from time import sleep
from telethon.tl.functions.users import GetFullUserRequest

# قم بتعديل هذه القيمة لتحديد عدد التحذيرات المسموح به
MAX_WARNINGS = 10

afkmode = set([])
allowed_users = set()  # قائمة المستخدمين المستثنين

@events.register(events.NewMessage(outgoing=True, pattern=r'\.تشغيل الرد'))
async def runafkon(event):
    await event.edit("انتظار...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    getreason = event.message.raw_text.splitlines()
    replacecmd = getreason[0].replace(".تشغيل الرد ", "")
    runafkon.afkreason = replacecmd.splitlines()
    runafkon.reason = runafkon.afkreason[0]
    try:
        if afkmode:
            if "off" in afkmode:
                afkmode.remove("off")
        afkmodeon = "on"
        if afkmodeon in afkmode:
            await event.client.send_message(messagelocation, "تم تنشيط وضع الرد التلقائي بالفعل وتم تحديث بياناتك قسراً")
        else:
            afkmode.add(afkmodeon)
            runafkon.start = datetime.now()
            await event.client.send_message(messagelocation, "تم تنشيط وضع الرد التلقائي")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.تعطيل الرد'))
async def runafkoff(event):
    await event.edit("جارٍ المعالجة...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        afkmodeoff = "off"
        if "on" in afkmode:
            afkmode.remove("on")
            runafkon.afkreason.clear()
        if afkmodeoff in afkmode:
            await event.client.send_message(messagelocation, "تم الغاء تنشيط الرد التلقائي بالفعل")
        else:
            afkmode.add(afkmodeoff)
            await event.client.send_message(messagelocation, "تم الغاء تنشيط الرد التلقائي ")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.الرد'))
async def runafkstatus(event):
    """
    هذه الدالة تظهر حالة وضع "بعيد عن لوحة المفاتيح" (AFK) الحالي.
    """
    if "on" in afkmode:
        await event.respond("وضع AFK مفعل حاليًا.")
        if runafkon.reason:
            await event.respond(f"السبب: {runafkon.reason}")
    else:
        await event.respond("وضع AFK معطل حاليًا.")

   except:
        pass
        
@events.register(events.NewMessage(outgoing=True, pattern=r'\.سماح'))
async def allow_user(event):
    """
    هذه الدالة تسمح لمستخدم محدد بإرسال الرسائل إليك دون الحصول على رد تلقائي.

    :param event: حدث الرسالة الواردة.
    """

    reply_to = await event.get_reply_message()
    if reply_to:
        user_id = reply_to.sender_id
        allowed_users.add(user_id)
        await event.respond(f"تم السماح للمستخدم {reply_to.sender.first_name} بإرسال الرسائل.")
    else:
        await event.respond("يجب عليك الرد على رسالة المستخدم الذي تريد السماح له.")
                
    except:   
        pass
        
@events.register(events.NewMessage(outgoing=True, pattern=r'\.الغاء_السماح'))
async def disallow_user(event):
    """
    هذا الدالة تقوم بإزالة مستخدم من قائمة المستثنين
    """
    reply_to = await event.get_reply_message()
    if reply_to:
        user_id = reply_to.sender_id
        if user_id in allowed_users:
            allowed_users.remove(user_id)
            await event.respond(f"تم إلغاء السماح للمستخدم {reply_to.sender.first_name}")
        else:
            await event.respond("هذا المستخدم ليس ضمن القائمة البيضاء")
    else:
        await event.respond("يجب الرد على رسالة المستخدم الذي تريد إلغاء السماح له")

   except:
       pass
      
@events.register(events.NewMessage)
async def runafk(event):
    """
    هذه الدالة هي المسؤولة عن التعامل مع رسائل المستخدمين عندما يكون البوت في وضع "بعيد عن لوحة المفاتيح" (AFK).

    :param event: حدث الرسالة الواردة.
    """

    if event.is_private:
        if "on" in afkmode:
            if user.id not in allowed_users:             
                warnings = 10
                await event.client.send_message(messagelocation, f"انا مشغول الان. كلمني فيما بعد. لديك {warnings} تحذيرات اذا بقيت مستمرا في الارسال سيتم حظرك", reply_to=replylocation)
