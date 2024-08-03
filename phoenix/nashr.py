import asyncio
from telethon.tl.functions.messages import broadcast

async def send_broadcast(client, message, seconds):
    while True:
        await asyncio.sleep(seconds)
        await client(broadcast(message=message))

async def handle_messages(client):
    @client.on(events.NewMessage)
    async def handler(event):
        if event.message.startswith('.نشر'):
            try:
                _, seconds = event.message.split()
                seconds = int(seconds)
                message = event.message.reply_to_msg_id
                await send_broadcast(client, message, seconds)
            except ValueError:
                await event.reply('أدخل عدد الثواني بصيغة رقمية.')

async def main():
    async with client:
        await handle_messages(client)

if __name__ == '__main__':
    from phoenix import client  # Assuming phoenix.py contains the client initialization
    asyncio.run(main())
