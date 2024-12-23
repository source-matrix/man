from telethon import events
import FINAL.client
import time
import os

client = FINAL.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.م17$'))
async def alive(event):
    client = event.client
    me = await client.get_me()
    username = me.username
    img = await client.download_profile_photo(username)
    time.sleep(0.5)
    await event.respond(f"""**
 <━━━[★] اوامر التنصيب [★]━━━>

هذا الاصدار يخص Termux او vps 
لن تحتاج هذه العملية للتنصيب لاشخاص اخرين 

**""", file=img, parse_mode="markdown")
    await event.message.delete()
    os.remove(img)
