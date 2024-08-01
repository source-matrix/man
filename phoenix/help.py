from telethon import events
import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def help(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""


<== **اوامر خدمية** ==>

 [1]الامر `.كتم` يقوم بكتم العضو مع تحديد الوقت ساعة يوم شهر  - (m, h, d)

 [2]الامر `.طرد` يسخدم للطرد داخل المجموعة

 [3]الامر `تشغيل الرد ` يقوم بتشغل الرد التلقائي للخاص 

[4] الامر `.تاك` يقوم بعمل تاك لكل اعضاء المجموعة 

[5] الامر `.تكرار` يقوم بالنشر التلقائي( الامر -الثواني -العدد-الرسالة )

[6]الامر ` .ايدي` يستخدم لعرض معلومات المستخدم(بالرد على الشخص)

[7]الامر `.واو` بيستخدم لحفظ الصور والفيديوهات المؤقته (بالرد على الصورة)

[++] لعرض اوامر التسلية  اكتب `.تسلية`

 




Developer: @I0I0II
"""))
