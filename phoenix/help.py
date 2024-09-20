from telethon import events
import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def help(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""**



 
༺☠️༻ FꙆ R E E U S E R B O T ༺☠️༻

┊ ✦ [1] `.اوامر الادمن` لاستعراض اوامر المجموعات والادمن

┊ ✦ [2] `.اوامر الخاص` لاستعراض اوامر الخاص والمحادثات الفردية

┊ ✦ [3] `.تسلية` لاستعراض اوامر التسلية والترفيه

┊ ✦ [4]  `.النشر` لاستعراض اوامر النشر بانواعة

┊ ✦ [5] الأمر `.واو` يستخدم لحفظ الصور والفيديوهات المؤقتة (بالرد على الصورة).

┊ ✦ [6] الأمر `.اسمي` / `.ايقاف اسمي` لوضع اسمك مع ساعة (الأمر مع الاسم الذي تريده).

┊ ✦ [7] `.تقليد` / `.الغاء التقليد ` يستخدم بالرد وسيقوم بتقليد جميع رسائل الشخص مهما كانت

┊ ✦ [8] `.انتحال`/`.اعادة` يستخدم بالرد على الشخص لانتحاله 

╰༺☠️༻ @I0I0II ༺☠️༻╯

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

@events.register(events.NewMessage(outgoing=True, pattern=".اوامر الخاص"))
async def kas(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""**

1 - `.تشغيل الرد` لتشغيل رد تلقائي تضعة انت سيظهر لكل من يقوم بمراسلتك

2 - `.كليشة الرد` لتعين كليشة الرد التلقائي [يستخدم بالرد على الرسالة]

3 - `.المخصص تشغيل` لتشغيل الردود المخصصة

4 - ` .رد ` الامر مع الرد الذي تود تخصيصة [يستعمل بالرد على اي رسالة ]

5 - ` .حذف رد` لحذف الردود التي قمت بتخصيصها سابقا

6 - ` .تعطيل الرد` لتعطيل كلاً من الردود المخصصة والرد التلقائي

7 - ` .اضف مجموعة التخزين ` بالرد على ايدي المجموعة -100

8 - ` .اضف اشتراك`/`.تعطيل الاشتراك` الامر مع معرف القناة @I0I0II  يجب ان يشترك ليتحدث معك

9 - ` .كتم ` سيقوم بكتم المستخدم داخل الخاص (بالرد على اي شخص)

10 - `.سماح` /`.الغاء السماح` يستخدم للسماح لشخص معين بارسال الرسائل لك بعد تشغيل الرد التلقائي

**"""))
@events.register(events.NewMessage(outgoing=True, pattern=".اوامر الادمن"))
async def mjm(event):
    await event.delete()
    messagelocation = event.to_id
    await event.client.send_message(messagelocation, ("""**

يجب ان تكون لديك صلاحية كافية للقيام بذلك 

تقييد - طرد - حظر -كتم
.الغاء -التقييد -الكتم -الحظر 
بالرد على المستخدم 
       **"""))
