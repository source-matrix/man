from telethon import events
import FINAL.client
import time
client = FINAL.client.client

@client.on(events.NewMessage(outgoing=True, pattern=".تاك_للكل"))
async def tagall(event):
    if not isinstance(event, events.NewMessage.Event):
        return
    client.parse_mode = "html"
    mentions = "<b>اعضاء المجموعة</b>\n"
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, 100):
        time.sleep(0.05)
        mentions += f" \n [{x.first_name}] (<a href='tg://user?id={x.id}'>Profile</a>)"
        time.sleep(0.05)
    await event.edit(mentions)
