from telethon import events
import FINAL.client
import time
client = FINAL.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.التنصيب'))
async def alive(event):
		client = event.client
		me = await client.get_me()
		username = me.username
		img = await client.download_profile_photo(username)
		time.sleep(0.5)
		await event.respond(f"""**Foydalanuvchi:** @{username}
**FINALUSERBOT:** https://t.me/i0i0ii 

**Developer:** @I0I0II 
			
v.1.2.0

📥 التثبيت 

$ `pkg update && pkg upgrade`

$ `apt update && apt upgrade`

$ `pkg install git`

$ `pkg install python`

$ `git clone https://github.com/1mrxe1/FINALv4`

$ `python setup.py`

$ `python main.py`""", file=img)
		await event.message.delete()
