import asyncio
from telethon import events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import FINAL

client = FINAL.client.client
update_tasks = {}

async def update_name_periodically(event, user_name):
    chat_id = event.chat_id
    while True:
        new_name = f"{user_name} {datetime.now().strftime('%I:%M')}"
        try:
            await event.client(UpdateProfileRequest(first_name=new_name))
        except Exception as ex:
            print(f"حدث خطأ: {str(ex)}")
        await asyncio.sleep(58)
        if chat_id in update_tasks and not update_tasks[chat_id]:
            break

@events.register(events.NewMessage(pattern=r".اسمي", outgoing=True))
async def change_name_with_time(event):
    if event.is_reply:
        original_message = await event.get_reply_message()
        user_name = original_message.text.strip() 
        chat_id = event.chat_id
        update_tasks[chat_id] = True
        asyncio.ensure_future(update_name_periodically(event, user_name))

@events.register(events.NewMessage(pattern=r".ايقاف اسمي", outgoing=True))
async def stop_name_update(event):
    chat_id = event.chat_id
    if chat_id in update_tasks:
        update_tasks[chat_id] = False
