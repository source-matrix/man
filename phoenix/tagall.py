from telethon import events
import phoenix.client
import time
client = phoenix.client.client

@events.register(events.NewMessage(pattern=".tagall"))
async def tagall(event):
		client.parse_mode = "html"
		if event.fwd_from:
			return
		mentions = "<b>Group members</b>\n"
		chat = await event.get_input_chat()
		async for x in client.iter_participants(chat, 100):
			time.sleep(0.05)
			mentions += f" \n [{x.first_name}] (<a href='tg://user?id={x.id}'>Profile</a>)"
			time.sleep(0.05)
			await event.edit(mentions)