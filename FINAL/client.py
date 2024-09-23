from telethon import TelegramClient, sync
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
import os
import pickle
import asyncio

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

def get_session_filename(phone_number):
    return f'session_{phone_number}.pkl'

def load_or_create_session(phone_number):
    filename = get_session_filename(phone_number)
    try:
        with open(filename, 'rb') as f:
            string = pickle.load(f)
        client = TelegramClient(StringSession(string), api_id, api_hash)
    except FileNotFoundError:
        string = input("Press enter to create a new session: ")
        client = TelegramClient(StringSession(string), api_id, api_hash)
    return client

def save_session(client, phone_number):
    filename = get_session_filename(phone_number)
    with open(filename, 'wb') as f:
        pickle.dump(client.session.save(), f)

def list_saved_sessions():
    session_files = [f for f in os.listdir() if f.startswith('session_') and f.endswith('.pkl')]
    if session_files:
        print("Saved sessions:")
        for i, session_file in enumerate(session_files):
            phone_number = session_file[8:-4]
            print(f"{i+1}. {phone_number}")
    else:
        print("No saved sessions found.")

while True:
    choice = input("\nDo you want to (A)dd a new session, (L)ist saved sessions, or (X) terminate a session? (A/L/X/E): ")
    if choice.lower() == 'e':
        break

    if choice.lower() == 'a':
        while True:
            phone_number = input("\033[032mPlease enter your phone (or bot token) or 'E' to return to the main menu: ")
            if phone_number.lower() == 'e':
                break

            client = load_or_create_session(phone_number)
            client.connect()

            if not client.is_user_authorized():
                client.send_code_request(phone_number)
                try:
                    client.sign_in(phone_number, input('\033[032mPlease enter the code you received: '))
                except SessionPasswordNeededError:
                    password = input('\033[032mPlease enter your password: ')
                    client.sign_in(password=password)

            save_session(client, phone_number)
            print(f"\033[032mSession for {phone_number} saved successfully!")

    elif choice.lower() == 'l':
        list_saved_sessions()
        session_files = [f for f in os.listdir() if f.startswith('session_') and f.endswith('.pkl')]
        if session_files:
            while True:
                try:
                    session_num = int(input("Enter the session number to run: "))
                    if 1 <= session_num <= len(session_files):
                        phone_number = session_files[session_num - 1][8:-4]
                        client = load_or_create_session(phone_number)
                        client.connect()
                        print(f"Session for {phone_number} started.")
                        # You can add further actions for the running session here if needed
                        break  # Exit the loop after running the chosen session
                    else:
                        print("Invalid session number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("No saved sessions found.")

    elif choice.lower() == 'x':
        list_saved_sessions()
        session_files = [f for f in os.listdir() if f.startswith('session_') and f.endswith('.pkl')]
        if session_files:
            while True:
                try:
                    session_num = int(input("Enter the session number to terminate: "))
                    if 1 <= session_num <= len(session_files):
                        phone_number = session_files[session_num - 1][8:-4]
                        filename = get_session_filename(phone_number)
                        os.remove(filename)
                        print(f"Session for {phone_number} terminated.")
                        break 
                    else:
                        print("Invalid session number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("No saved sessions found.")

    else:
        print("Invalid choice. Please enter A, L, X, or E.")
