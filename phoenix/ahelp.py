from telethon import events

import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".رسوم"))
async def ahelp(event):
	client.parse_mode = "html"
	await event.delete()
	messagelocation = event.to_id
	await event.client.send_message(messagelocation, ("""
<b>قائمة الرسوم المتحركة</b>
[01] فن الوحش - .monster
[02] فن الخنزير - .pig
[03] فن القاتل - .killer
[04] فن السلاح - .gun
[05] فن الكلب - .dog
[06] مرحباً كبيراً -.welc
[07] مرحبا صديقي الفن - .hmf
[08] فن الزوجين - .couple
[09] فن السوبرمي - .sup
[10] نص الترحيب - .welc
[11] فن الثعبان - .asnake
[12] فن القطط - .cat
[13] نص الوداع - .bye
[14] فن شيتوس - .shitos
[15] لا أحب bigf - .dislike
[16] التنويم المغناطيسي - .hypno
[17] sq - .squ
[18] كيلر - .kiler
[19] قطار متحرك - .train
[20] الرسوم المتحركة الغريبة - .rocket
[21] قلب متحرك - .hart
[22] حيوان مُغتصب - .raped
[23] FNL - .fnl
[24] قرد متحرك - .monkey
[25] الأيدي المتحركة - .hands
[26] عدد الأرقام - .count
[27] اففف كبير - .kf
[28] اف اف -.f {نص}
[29] عطلة كبيرة - .bigoff
[30] زهرة - .flower {نص}
[31] قلوب متحركة - .vheart {نص}
[32] أحبك  أنمي - .luvart {نص}
[33] أحبك  - .iloveu
<b>المطور:</b> @I0I0II 
"""))
