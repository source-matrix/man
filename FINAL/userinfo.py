from telethon import events
import FINAL.client
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.types import InputPeerUser

client = FINAL.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.ايدي'))
async def userinfo(event):
    await event.delete()
    try:
        getinformation = await event.get_reply_message()
        targetid = getinformation.sender_id
        targetdetails = await client(GetFullUserRequest(targetid))
        messagelocation = event.to_id
        client.parse_mode = "html"

        user_entity = targetdetails.users[0]
        user_photo = await client.download_profile_photo(InputPeerUser(user_entity.id, user_entity.access_hash))


        photos = await client(GetUserPhotosRequest(user_id=targetid, offset=0, max_id=0, limit=100))
        image_count = len(photos.photos)

        message_text = f"""
ٴ⋆─┄─┄─┄─ FINAL ─┄─┄─┄─⋆

✦ الاسـم    ⇠  {targetdetails.users[0].first_name}
✦ المعـرف  ⇠  @{targetdetails.users[0].username}
✦ الايـدي   ⇠  {targetdetails.users[0].id}
✦ الصـور    ⇠  {image_count}
✦ التفاعل   ⇠  امبراطور التفاعل  🥇
✦ الـمجموعات المشتـركة ⇠  {targetdetails.full_user.common_chats_count}
✦ البايـو     ⇠  {targetdetails.full_user.about}

ٴ⋆─┄─┄─┄─ FINAL ─┄─┄─┄─⋆
"""

        if user_photo:
            await client.send_message(messagelocation, message_text, file=user_photo)
        else:
            await client.send_message(messagelocation, message_text)

    except Exception as e:
        print(f"Error in userinfo: {e}")
        await event.respond(f"حدث خطأ: {e}")
