from telethon import events
import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def help(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""**


<== اوامر بسيطة ==>


 [1]الامر `.كتم` يقوم بكتم العضو مع تحديد الوقت ساعة يوم شهر  - (m, h, d)

 [2]الامر `.طرد` يسخدم للطرد داخل المجموعة

 [3]الامر `.تشغيل الرد ` يقوم بتشغل الرد التلقائي للخاص 

[4] الامر `.تاك` يقوم بعمل تاك لكل اعضاء المجموعة 

[5]الامر ` .ايدي` يستخدم لعرض معلومات المستخدم(بالرد على الشخص)

[6]الامر `.واو` بيستخدم لحفظ الصور والفيديوهات المؤقته (بالرد على الصورة)

[7]الامر `.اسمي` يسخدم لتغيير اسمك على شكل ساعة  (الامر مع الاسم الذي تريده)

[++] اكتب `.النشر`  لاستعراض انواع النشر

[++] اكتب `.تسلية` لاستعراض اوامر التسلية 


Developer: @I0I0II
**"""))

@events.register(events.NewMessage(outgoing=True, pattern=".فحص"))
async def hi(event):
    await event.delete()
    messagelocation = event.to_id

    # لك الحمد مهما استطال البلاء
    video_path = "https://t.me/N1NN_N/4"  
    video_caption = "انا والسورس في خدمتك اكت `.الاوامر`"

    # يابقية الله
    await event.client.send_file(messagelocation, video_path, caption=video_caption)


        
