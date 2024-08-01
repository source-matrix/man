from telethon import events
from time import sleep
from telethon.tl.functions.users import GetFullUserRequest
import phoenix.client
client = phoenix.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.طرد'))
async def runkick(event):
    await event.edit("جارٍ...")
    sleep(2)
    await event.delete()
    getmessage = await event.get_reply_message()
    targetuser = getmessage.sender_id
    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    getreason = event.message.raw_text.splitlines()
    replacecmd = getreason[0].replace(".طرد ", "")
    kickedreason = replacecmd.splitlines()
    reason = kickedreason[0]
    client.parse_mode = "html"
    try:
        await event.client.kick_participant(messagelocation, getmessage.sender.id)
        if reason:
            if ".طرد" in reason:
                await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> تم ركله")
            else:
                await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> تم ركله\nسبب: {reason}")
        else:
            await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> تم تنفيذ الركلة")
    except:
        pass
