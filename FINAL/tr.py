from gpytranslate import Translator
from telethon import events



@events.register(events.NewMessage(pattern=".ترجم"))
async def tr(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.edit("`.tr LanguageCode` as reply to a message")
        return
    lan = lan.strip()
    translator = Translator()
    try:
        translated = await translator(text, targetlang=lan)

        after_tr_text = translated.text
        source_lan = await translator.detect(f'{translated.orig}')
        transl_lan = await translator.detect(f'{translated.text}')
        output_str = "لغة الرسالة: **{}**\nمترجمة: **{}**\n\nرسالة: {}".format(
            source_lan,
            transl_lan,
            after_tr_text
        )
        await event.edit(output_str)
    except Exception as exc:
        await event.edit(str(exc))
