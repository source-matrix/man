from telethon import events
import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def help(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""**



 
༺☠️༻ FꙆ R E E U S E R B O T ༺☠️༻
┊ ✦ [1] الأمر `.طرد` يستخدم للطرد داخل المجموعة.

┊ ✦ [2] الأمر `.تشغيل الرد` يقوم بتشغيل الرد التلقائي للخاص.

┊ ✦ [3] الأمر `.تاك` يقوم بعمل تاك لكل أعضاء المجموعة.

┊ ✦ [4] الأمر `.ايدي` يستخدم لعرض معلومات المستخدم (بالرد على الشخص).

┊ ✦ [5] الأمر `.واو` يستخدم لحفظ الصور والفيديوهات المؤقتة (بالرد على الصورة).

┊ ✦ [6] الأمر `.اسمي` يستخدم لتغيير اسمك على شكل ساعة (الأمر مع الاسم الذي تريده).

┊ ✦ [7] الأمر `.تقييد` / `.الغاء التقييد` لتقييد المستخدم داخل المجموعات والقنوات.

┊ ✦ [8] الأمر `.اضف مجموعة التخزين` بالرد على ايدي المجموعة التي تريدها لتخزين الرسائل.

┊ ✦ [9] الأمر `.المخصص تشغيل` لتشغيل الردود المخصصة.

┊ ✦ [10] الأمر `.كليشة الرد` بالرد على أي كليشة، سيقوم بتعيينها كرسالة تظهر لكل من يقوم بمراسلتك على الخاص.

┊ ✦ [11] الأمر `.تعطيل الرد` لتعطيل كلا من الرد التلقائي والردود المخصصة.

┊ ✦ [12] الأمر `.رد (مثلا هلو)` بالرد على أي رسالة مثلا "أهلا"، سيقوم بإرسال "هلو" كلما أرسل أحد إليك "أهلا".

╰༺☠️༻ 🅕🅘🅝🅐🅛 ༺☠️༻╯

* [++] اكتب `.النشر` لاستعراض أنواع النشر.

* [++] اكتب `.تسلية` لاستعراض أوامر التسلية.


Deve: @I0I0II 


**"""))

@events.register(events.NewMessage(outgoing=True, pattern=".فحص"))
async def hi(event):
    await event.delete()
    messagelocation = event.to_id

    # لك الحمد مهما استطال البلاء
    video_path = "https://t.me/N1NN_N/4"  
    video_caption = "انا والسورس في خدمتك اكتب `.الاوامر`"

    # يابقية الله
    await event.client.send_file(messagelocation, video_path, caption=video_caption)


        
