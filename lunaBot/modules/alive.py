import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/e57fffe4b3f6189311c23.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  xxx = "**❄𝗛𝗼𝗶𝗶, 𝗜 𝗮𝗺 ⏤‌★GODZILLA☆「🇮🇳」𝗥𝗼𝗯𝗼𝘁!!❄ !** \n\n"
  xxx += "🔴 **❄ ✘ 𝗜'𝗺 𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗶𝗻 𝗪𝗲𝗹𝗹 𝗠𝗮𝗻𝗻𝗲𝗿!** \n\n"
  xxx += "🔴 ** ❄ ✘ 𝗛𝘂𝗶 𝗛𝘂𝗶 𝗠𝘆 𝗠𝗮𝘀𝘁𝗲𝗿 : [AJAY](https://t.me/XXXTENTACION_FOREVER)** \n\n"
  xxx += f"🔴 ** ❄ ✘ 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻 𝗩𝗲𝗿𝘀𝗶𝗼𝗻: {tlhver}** \n\n"
  xxx += f"🔴 **❄ ✘ 𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 : {pyrover}** \n\n"
  xxx += "**❄「𝗧𝗵𝗮𝗻𝘅𝘅 𝗙𝗼𝗿 𝗨𝘀𝗶𝗻𝗴 𝗠𝗲 𝘀𝘂𝗿」❤️❄**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/godzilla_x_robot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/godzilla_chatting")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=godzilla,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  LUNA = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/insane_bots")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=godzilla,  buttons=BUTTON)
