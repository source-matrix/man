from telethon import events
import phoenix.client
from datetime import datetime

client = phoenix.client.client


@events.register(events.NewMessage(pattern='\.ping'))
async def ping(event):
    client.parse_mode = "html"
    start = datetime.now()
    msg = await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"<b>Pong!!<b/>\n`{ms} ms`")
