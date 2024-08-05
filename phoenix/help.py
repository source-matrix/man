from telethon import events
import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def help(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""


<== *اوامر بسطة** ==>


 [1]الامر `.كتم` يقوم بكتم العضو مع تحديد الوقت ساعة يوم شهر  - (m, h, d)

 [2]الامر `.طرد` يسخدم للطرد داخل المجموعة

 [3]الامر `.تشغيل الرد ` يقوم بتشغل الرد التلقائي للخاص 

[4] الامر `.تاك` يقوم بعمل تاك لكل اعضاء المجموعة 

[5]الامر ` .ايدي` يستخدم لعرض معلومات المستخدم(بالرد على الشخص)

[6]الامر `.واو` بيستخدم لحفظ الصور والفيديوهات المؤقته (بالرد على الصورة)

[++] اكتب `.النشر`  لاستعراض انواع النشر

[++] اكتب `.تسلية` لاستعراض اوامر التسلية 


Developer: @I0I0II
"""))
@events.register(events.NewMessage(outgoing=True, pattern=".فحص"))
async def hi(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""
        السورس يعمل جيدا .اكتب `.الاوامر` 
        """))
        @events.register(events.NewMessage(outgoing=True, pattern=".فحص"))
async def hip(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""
        **انواع النشر المتوفر**

ء--------——————————----
1-الامر  `.نشر` يقوم بالنشر بكل المجموعات لديك دفعة واحده (الامر-الثواني-العدد-الرسالة)
مثال .نشر 5 10 هلو
ء--------——————————----
2-الامر `.تناوب` يعمل للنشر في كل المجموعات بالتسلسل واحد بعد الاخرى.. هذا الخيار الافضل لتجنب حذف الحساب والحظر (الامر-الثواني -العدد -الرسالة)
 ء--------——————————----
3- الامر `.تكرار` يقوم بتكرار الرسالة بنفس المكان ( الامر -الثواني -العدد-الرسالة )
ء--------——————————----
**ملاحظة**
لاتحتوي العمليات الثلاث (تكرار و نشر و تناوب ) على خيار الايقاف لذلك كن حذرا مع العدد الذي تضعه ابتعد عن الارقام 999 بل ضع عددا يناسب عملك كـ20او 30 لانه كما اخبرتك سابقا لن تتوقف عملية النشر حتى ينتهي العدد الذي تضعة . 
        """))
