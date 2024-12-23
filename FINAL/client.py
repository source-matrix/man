from telethon import TelegramClient, events, sync 
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
import os
import pickle
import sys

api_id = 29914850
api_hash = "de7b0ee6f49fff7b4a5f0e5c015972ce"

os.system("clear")
print("""\033[031m

─────▄████▀█▄
───▄█████████████████▄
─▄█████.▼.▼.▼.▼.▼.▼▼▼▼
███████    𝙁𝙄𝙉𝘼𝙇𝙐𝙎𝙍𝘽𝙊𝙏
████████▄▄▲.▲▲▲▲▲▲▲
████████████████████▀▀


𝐃𝐞𝐯: @𝐈𝟎𝐈𝟎𝐈𝐈
""")

def get_session_filename(phone_number):
    return f'session_{phone_number}.pkl'

def load_or_create_session(phone_number):
    filename = get_session_filename(phone_number)
    try:
        with open(filename, 'rb') as f:
            string = pickle.load(f)
        client = TelegramClient(StringSession(string), api_id, api_hash)
        print(f"\033[032mSession for {phone_number} loaded successfully!")
        return client
    except FileNotFoundError:
        client = TelegramClient(StringSession(), api_id, api_hash)
        return client

while True:
    phone_number = input("\033[032mPlease enter your phone (or bot token): ") 
    client = load_or_create_session(phone_number)
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        try:
            client.sign_in(phone_number, input('\033[032mPlease enter the code you received: '))
        except SessionPasswordNeededError:
            password = input('\033[032mPlease enter your password: ')
            client.sign_in(password=password)

        with open(get_session_filename(phone_number), 'wb') as f:
            pickle.dump(client.session.save(), f)
        print(f"\033[032mSession for {phone_number} saved successfully!")

    print(f"Session for {phone_number} started.")
    break  # Exit the loop after starting the session
