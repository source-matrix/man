from telethon import events
import time
import asyncio
import random
import FINAL.client

client = FINAL.client.client

@events.register(events.NewMessage(pattern='\.تحميل|\.هاك', outgoing=True))
async def loading(event: events.NewMessage.Event):
    try:
        if event.pattern_match.group(0) == ".تحميل":
            percentage = 0
            while percentage < 100:
                temp = 100 - percentage
                temp = temp if temp > 5 else 5
                percentage += temp / random.randint(5, 10)
                percentage = round(percentage, 2)
                progress = int(percentage // 5)
                await event.edit(f'`|{"█" * progress}{"-" * (20 - progress)}| {percentage}%`')
                await asyncio.sleep(.5)
            time.sleep(5)
            await event.delete()

        elif event.pattern_match.group(0) == ".هاك":
            if event.reply_to_msg_id:
                reply_message = await event.get_reply_message()
                idd = reply_message.sender_id
                if idd == 705475246:
                    await event.edit("**᯽︙ عـذرا لا استـطيع اخـتراق مـطوري اعـتذر او سيقـوم بتهـكيرك**")
                    return
                await event.edit("يتـم الاختـراق ..")
                sender = await event.get_sender()
                first_name = sender.first_name
                animation_chars = [
                    "᯽︙ تـم الربـط بسـيرفرات الـتهكير الخـاصة",
                    "تـم تحـديد الضحـية",
                    "**تهكيـر**... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                    "**تهكيـر**... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                    "**تهكيـر**... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                    "**تهكيـر**... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                    "**تهكيـر**... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                    "**تهكيـر**... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
                    "**تهكيـر**... 84%\n█████████████████████▒▒▒▒ ",
                    "**تهكيـر**... 100%\n████████████████████████ ",
                    f"᯽︙ ** تـم اخـتراق الضـحية**..\n\nقـم بالـدفع الى {first_name} لعـدم نشـر معلوماتك وصـورك",
                ]
                animation_interval = 3
                animation_ttl = range(len(animation_chars))
                for i in animation_ttl:
                    await asyncio.sleep(animation_interval)
                    await event.edit(animation_chars[i])
                time.sleep(5)
                await event.delete()
            else:
                await event.edit("᯽︙ لم يتـم التعـرف على المستـخدم")
    except Exception as e:
        print(e)
