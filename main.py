from os import environ
from pyrogram import Client, idle

API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
SESSION_STRING = environ["SESSION_STRING"]  # Corrected variable name

PLUGINS = dict(
    root="plugins",
    include=[
        "vc." + environ["PLUGIN"],
        "ping",
        "sysinfo"
    ]
)

app = Client("userbot", session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH, plugins=PLUGINS)

app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
