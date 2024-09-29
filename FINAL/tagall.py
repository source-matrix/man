from telethon import events
import FINAL.client
import asyncio
import telethon.tl.types

client = FINAL.client.client

@client.on(events.NewMessage(outgoing=True, pattern=".تاك_للكل"))
async def tagall(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    client.parse_mode = "html"
    mentions = "<b>أعضاء المجموعة:</b>\n"
    chat = await event.get_input_chat()

    me = await client.get_me()
    permissions = await client.get_permissions(chat, me)

    if not (permissions.is_admin and permissions.add_admins):  
        await event.edit("عذرًا، لا أملك صلاحية ذكر الجميع في هذه المجموعة.")
        return

    all_participants = await client.get_participants(chat)
    total_members = len(all_participants)

    hidden_members_found = False

    for i in range(0, total_members, 100):
        batch = all_participants[i:i+100]
        mentions_batch = ""
        for user in batch:
            if user.deleted:
                continue
            try:
                participant = await client.get_entity(user.id)  
                if isinstance(participant, telethon.tl.types.ChannelParticipant) and participant.is_hidden:  
                    hidden_members_found = True
            except ValueError:
                continue
            mentions_batch += f"<a href='tg://user?id={user.id}'>{user.first_name}</a> "

        # الساعة بـ4:03ص كنت هنا
        mentions += mentions_batch  
        await event.edit(mentions)
        await asyncio.sleep(0.7)

    if hidden_members_found:
        mentions += "(لا يمكن ذكر الأعضاء المخفيين)\n"

    await event.edit(mentions)  
