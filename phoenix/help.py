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

 [3]الامر `.تشغيل الرد ` يقوم بتشغل الرد التلقائي للخاص 

[4] الامر `.تاك` يقوم بعمل تاك لكل اعضاء المجموعة 

[5] الامر `.تكرار` يقوم بتكرار الرسالة( الامر -الثواني -العدد-الرسالة )

[6]الامر ` .ايدي` يستخدم لعرض معلومات المستخدم(بالرد على الشخص)

[7]الامر `.واو` بيستخدم لحفظ الصور والفيديوهات المؤقته (بالرد على الصورة)

[8](الامر `.تناوب` يعمل للنشر في كل المجموعات بالتسلسل ينشر في الاولى ونتقل للثانية الخ.. هذا الخيار لتجنب الحظر (الامر-العدد-الثواني -الرسالة 

[9](الامر `.نشر` يقوم بالنشر بكل المجموعات لديك دفعة واحده (الامر-الوقت-العدد-الرسالة

[++] لعرض اوامر التسلية  اكتب `.تسلية`


Developer: @I0I0II
"""))
@events.register(events.NewMessage(outgoing=True, pattern=".فحص"))
async def hi(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""
        جميع `.الاوامر` تعمل اتمنى لك وقتا طيبا 
        """))
