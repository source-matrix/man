from telethon import events
from time import sleep
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
import FINAL.client
client = FINAL.client.client


@events.register(events.NewMessage(outgoing=True, pattern=r'\.(حظر|طرد|تقييد)'))
async def runkick(event):
    await event.edit("جارٍ...")
    await event.delete()
    command = event.pattern_match.group(1)
    getmessage = await event.get_reply_message()

    if getmessage:
        targetuser = getmessage.sender_id
    else:  
        try:
            
            targetuser = int(event.text.split(" ", 1)[1])
        except (ValueError, IndexError):
            
            if event.message.entities:
                for entity in event.message.entities:
                    if hasattr(entity, 'user_id'):
                        targetuser = entity.user_id
                        break
                    elif hasattr(entity, 'username'):
                        try:
                            targetuser = (await client.get_entity(
                                entity.username)).id
                            break
                        except ValueError:
                            await event.respond(
                                "لم يتم العثور على مستخدم بهذا الاسم.")
                            return
            else:  
                await event.respond(
                    "يرجى الرد على المستخدم لاتمام الامر"
                )
                return

    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    getreason = event.message.raw_text.splitlines()
    replacecmd = getreason[0].replace(f".{command} ", "")
    reason = replacecmd.splitlines()[0]
    client.parse_mode = "html"

    try:
        if command == "طرد":
            await event.client.kick_participant(messagelocation, targetuser)
            action = "تم طرده"
        elif command == "حظر":
            await client(EditBannedRequest(messagelocation, targetuser,
                                           ChatBannedRights(
                                               until_date=None,
                                               view_messages=True)))
            action = "تم حظره"
        elif command == "تقييد":
            await client(EditBannedRequest(messagelocation, targetuser,
                                           ChatBannedRights(
                                               until_date=None,
                                               send_messages=True)))
            action = "تم تقييده"

        if reason:
            if f".{command}" in reason:
                await event.client.send_message(
                    messagelocation,
                    f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}"
                )
            else:
                await event.client.send_message(
                    messagelocation,
                    f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}\nسبب: {reason}"
                )
        else:
            await event.client.send_message(
                messagelocation,
                f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}"
            )

    except Exception as e:
        await event.respond(f"حدث خطأ: {e}")


@events.register(events.NewMessage(outgoing=True, pattern=r'\.(الغاء الحظر|الغاء التقييد)'))
async def unrunkick(event):
    await event.edit("جارٍ...")
    await event.delete()
    command = event.pattern_match.group(1)
    getmessage = await event.get_reply_message()

    if getmessage:
        targetuser = getmessage.sender_id
    else:  
        try:
            
            targetuser = int(event.text.split(" ", 1)[1])
        except (ValueError, IndexError):
            
            if event.message.entities:
                for entity in event.message.entities:
                    if hasattr(entity, 'user_id'):
                        targetuser = entity.user_id
                        break
                    elif hasattr(entity, 'username'):
                        try:
                            targetuser = (await client.get_entity(
                                entity.username)).id
                            break
                        except ValueError:
                            await event.respond(
                                "لم يتم العثور على مستخدم بهذا الاسم.")
                            return
            else: 
                await event.respond(
                    ". يرجى الرد على المستخدم"
                )
                return

    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    client.parse_mode = "html"

    try:
        await client(EditBannedRequest(messagelocation, targetuser,
                                       ChatBannedRights(
                                           until_date=None,
                                           view_messages=False,
                                           send_messages=False)))

        if command == "الغاء الحظر":
            action = "تم إلغاء حظره"
        elif command == "الغاء التقييد":
            action = "تم إلغاء تقييده"

        await event.client.send_message(
            messagelocation,
            f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}"
        )

    except Exception as e:
        await event.respond(f"حدث خطأ: {e}")

    client.parse_mode = "markdown"  # إعادة تعيين parse_mode إلى Markdown
