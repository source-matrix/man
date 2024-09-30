from telethon import events
import FINAL.client
import asyncio
import telethon.tl.types

client = FINAL.client.client

@client.on(events.NewMessage(outgoing=True, pattern=r"(.تاك_للكل|.all)(.*)"))
async def tagall(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    client.parse_mode = "html"
    message_text = event.pattern_match.group(2).strip()
    mentions = ""
    chat = await event.get_input_chat()
    me = await client.get_me()
    permissions = await client.get_permissions(chat, me)

    if not permissions.is_admin:
        await event.edit("عذرًا، لا أملك صلاحية ذكر الجميع في هذه المجموعة.")
        return

    all_participants = await client.get_participants(chat)
    total_members = len(all_participants)
    hidden_members_found = False
    all_mentions = []
    for user in all_participants:
        if user.deleted:
            continue
        try:
            participant = await client.get_entity(user.id)
            if isinstance(participant, telethon.tl.types.ChannelParticipant) and participant.is_hidden:
                hidden_members_found = True
        except ValueError:
            continue
        all_mentions.append(f"<a href='tg://user?id={user.id}'>{user.first_name}</a>")
    mentions_lists = [all_mentions[i:i+100] for i in range(0, total_members, 100)]
    final_mentions = ""
    for mentions_list in mentions_lists:
        if message_text:
            final_mentions += f"<b>{message_text}</b>\n"
        final_mentions += " ".join(mentions_list) + "\n\n" 

    if hidden_members_found:
        final_mentions += "(لا يمكن ذكر الأعضاء المخفيين)\n"

    # الساعة ب ٤:٢٠ تعبتتتتتتت
    await event.edit(final_mentions)
