import re
from pyrogram import filters
import random
from DAXXMUSIC import app


@app.on_message(filters.command(["gn","n","oodnight","ood Night","ood night"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**𝐆𝐨𝐨𝐝𝐍𝐢𝐠𝐡𝐭 𝐃𝐞𝐚𝐫 💕, {sender}! 𝐒𝐥𝐞𝐞𝐩 𝐭𝐢𝐠𝐡𝐭. 🌙🥀💝**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**𝐆𝐨𝐨𝐝𝐍𝐢𝐠𝐡𝐭 𝐃𝐞𝐚𝐫 💕, {sender}! 𝐒𝐥𝐞𝐞𝐩 𝐭𝐢𝐠𝐡𝐭. {emoji}**")


def get_random_sticker():
    stickers = [
        "CAACAgUAAx0Cc_auxAABAkR4ZeS6qZFzI8EZqXITWuRgr550HY0AAvYIAALaXkhVRTThG9g16V00BA", # Sticker 1
        "CAACAgIAAx0Ce9_hCAACaEplwn7dvj7G0-a1v3wlbN281RMX2QACUgwAAligOUoi7DhLVTsNsh4E", # Sticker 2
        "CAACAgIAAx0Ce9_hCAACaFBlwn8AAZNB9mOUvz5oAyM7CT-5pjAAAtEKAALa7NhLvbTGyDLbe1IeBA", # Sticker 3
        "CAACAgUAAx0CcmOuMwACldVlwn9ZHHF2-S-CuMSYabwwtVGC3AACOAkAAoqR2VYDjyK6OOr_Px4E",
        "CAACAgIAAx0Ce9_hCAACaFVlwn-fG58GKoEmmZpVovxEj4PodAACfwwAAqozQUrt2xSTf5Ac4h4E",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "😴",
        "😽",
        "💤",
    ]
    return random.choice(emojis)
