#MIT License

#Copyright (c) 2024 deleted-account

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import time
from datetime import datetime
import asyncio
from urllib.parse import quote

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from config import CMD_HANDLER
from config import SUDO_USERS
from config import BOT_VER, BRANCH as brch
from X import CMD_HELP, StartTime
from X.helpers.basic import edit_or_reply
from X.helpers.constants import WWW
from X.helpers.PyroHelpers import SpeedConvert
from X.modules.bot.inline import get_readable_time
from X.helpers.adminHelpers import DEVS

from .help import *

modules = CMD_HELP

def get_localization(language):
    if language == "en":  # English localization
        return {
            "server_11": "» ʀᴜɴɴɪɴɢ ᴀ sᴘᴇᴇᴅᴛᴇsᴛ...",
            "server_12": "⇆ ʀᴜɴɴɪɴɢ ᴜᴩʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...",
            "server_13": "⇆ ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...",
            "server_14": "↻ sʜᴀʀɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs...",
            "server_15": "✯ sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs ✯\n\n"
                         "ᴄʟɪᴇɴᴛ :\n"
                         "» ɪsᴩ :  {}\n"
                         "» ᴄᴏᴜɴᴛʀʏ :  {}\n\n"
                         "sᴇʀᴠᴇʀ :\n"
                         "» ɴᴀᴍᴇ : {}\n"
                         "» ᴄᴏᴜɴᴛʀʏ : {}\n"
                         "» sᴩᴏɴsᴏʀ : {}\n"
                         "» ʟᴀᴛᴇɴᴄʏ : {}\n"
                         "» ᴩɪɴɢ :  {} ms"
        }
    # Add more language options as needed

def testspeed(m, _):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit_text(_["server_12"])
        test.download()
        m = m.edit_text(_["server_13"])
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit_text(_["server_14"])
    except Exception as e:
        return m.edit_text(f"<code>{e}</code>")
    return result
    
@Client.on_message(
    filters.command(["speedtest"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def speedtest_function(client, message: Message):
    _ = get_localization("en")
    m = await message.reply_text(_["server_11"])
    loop = asyncio.get_event_loop()
    try:
        result = await loop.run_in_executor(None, testspeed, m, _)
        output = _["server_15"].format(
            result.get("client", {}).get("isp", "N/A"),
            result.get("client", {}).get("country", "N/A"),
            result.get("server", {}).get("name", "N/A"),
            result.get("server", {}).get("country", "N/A"),
            result.get("server", {}).get("cc", "N/A"),
            result.get("server", {}).get("sponsor", "N/A"),
            result.get("server", {}).get("latency", "N/A"),
            result.get("ping", "N/A"),
        )
        msg = await message.reply_photo(photo=result.get("share"), caption=output)
    except Exception as e:
        await m.edit_text(f"Error occurred: {e}")
    finally:
        await m.delete()
        


@Client.on_message(
    filters.command(["dc"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(
    filters.command("Cpink", [""]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(
    filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"🏓 ** ᴘɪɴɢ ᴘᴏɴɢ!!**\n"
        f"**├• ** `%sms`\n"
        f"╰•** 💻 ᴍᴀsᴛᴇʀ :** {client.me.mention}" % (duration)
    )


@Client.on_message(filters.command("Cping", [""]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(
    filters.command(["pink"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def pink(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    X = await message.reply("**sᴀʙᴀʀʀ ᴅᴏɢ ʟᴀɢɢɪɴɢ...**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await X.edit(
        f"**🏓 ᴘɪɴɢ ᴘᴏɴɢ**\n"
        f"**├• ᴘɪɴɢ  :** "
        f"`%sms` \n"
        f"**├•  ᴜᴘᴛɪᴍᴇ  :** "
        f"`{uptime}` \n"
        f"**└•  ᴍᴀsᴛᴇʀ   :** {client.me.mention}" % (duration)
    )
  

@Client.on_message(
    filters.command("Ceping", [""]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(
    filters.command(["pong"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def X(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(message, "ᴅᴇᴀʀ ᴄᴏᴄᴏᴋɪɴ")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    await xx.edit("8==✊=D")
    await xx.edit("8=✊==D")
    await xx.edit("8✊===D")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    await xx.edit("8==✊=D")
    await xx.edit("8=✊==D")
    await xx.edit("8✊===D")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    await xx.edit("**ᴀʜʜ ɪ'ᴍ ɢᴏɪɴɢ ᴛᴏ ᴄʀᴏᴛ**")
    await xx.edit("8===✊D💦")
    await xx.edit("8====D💦💦")
    await xx.edit("**ᴄʀᴏᴏᴛᴛᴛᴛ**")
    await xx.edit("**ᴄʀᴏᴏᴛᴛᴛᴛ ᴀᴀᴀʜʜʜ.....**")
    await xx.edit("ᴀʜʜʜ ᴇɴᴀᴋᴋᴋᴋᴋ ᴅᴀʀʟɪɴɢɢɢɢ🥵🥵")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit
