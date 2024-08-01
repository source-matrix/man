from telethon import events 
from telethon.tl.functions.account import UpdateProfileRequest
import phoenix.client
import time

client = phoenix.client.client
@events.register(events.NewMessage(pattern=r".تغيير الاسم (.*)", outgoing=True))
async def rename(event):
    ok = await event.edit("تغيير اللقب...")
    names = event.pattern_match.group(1).strip() 
    first_name = names
    last_name = ""
    if "/" in names:
        first_name, last_name = names.split("/", 1)
        await event.edit('تغير الاسم')
    try:
        await event.client(UpdateProfileRequest(first_name=first_name, last_name=last_name,)) 
        await event.edit('تغير الاسم بنجاح')
    except Exception as ex:
        await event.edit(ok, "\n`{}`".format(str(ex)))
    time.sleep(0.5)
    await event.delete()
