import asyncio
from telethon import events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import phoenix

client = phoenix.client.client

async def update_name_periodically(event):
    user_name = event.pattern_match.group(1)
    while True:
        new_name = f"{user_name} {datetime.now().strftime('%I:%M')}"
        try:
            await event.client(UpdateProfileRequest(first_name=new_name))
        except Exception as ex:
            print(f"حدث خطأ: {str(ex)}")
        await asyncio.sleep(59)

@events.register(events.NewMessage(pattern=r".اسمي (.*)", outgoing=True))
async def change_name_with_time(event):
    asyncio.ensure_future(update_name_periodically(event))
