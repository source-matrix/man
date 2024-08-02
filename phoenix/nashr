from telethon import events
import phoenix.client
import asyncio
import time

client = phoenix.client.client  # تأكد من تهيئة العميل بشكل صحيح

async def send_messages(message, interval):
    while True:
        for dialog in await client.get_dialogs():
            if dialog.is_group:
                await client.send_message(dialog, message)
        await asyncio.sleep(interval)

async def main():
    while True:
        command = input("أدخل الأمر (.نشر لبدء النشر، .ايقاف للتوقف): ")
        if command == ".نشر":
            message = input("أدخل الرسالة: ")
            interval = int(input("أدخل الفترة الزمنية بين الرسائل بالثواني: "))
            asyncio.create_task(send_messages(message, interval))
        elif command == ".ايقاف":
            break

if __name__ == "__main__":
    asyncio.run(main())
