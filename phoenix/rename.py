from telethon import events
from telethon.tl.functions.account import UpdateProfileRequest
import phoenix.client
import time
from datetime import datetime

client = phoenix.client.client

@events.register(events.NewMessage(pattern=r".اسمي (.*)", outgoing=True))
async def change_name_with_time(event):
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        user_name = event.pattern_match.group(1)
        new_name = f"{user_name} {current_time}"
        try:
            await event.client(UpdateProfileRequest(first_name=new_name))
        except Exception as ex:
            print(f"حدث خطأ: {str(ex)}")
        time.sleep(60)  


