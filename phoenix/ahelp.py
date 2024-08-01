from telethon import events

import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".تسلية"))
async def ahelp(event):
	client.parse_mode = "html"
	await event.delete()
	messagelocation = event.to_id
	await event.client.send_message(messagelocation, ("""
<b>قائمة التسلية</b>
**ضع دوت (نقطة) قبل كل امر**

وحش - خنزير  - قاتل - سلاح  -كلب - هلو همف - زوج- رشفة - مرحبا - ثعبان -قطة -همم - وداعا - شيتوز  -دسلايك - هينفو- النظام الشمسي - جيو - شرطة - طائرة - صندوق - مطر- احبك - فلايفمي - منصة - فراشة - قنبلة - احمق - ايموجي - احم - احبك2 - ذهبت - حب - سحر - تفاعل - ثلج
<b>المطور:</b> @I0I0II 
"""))
