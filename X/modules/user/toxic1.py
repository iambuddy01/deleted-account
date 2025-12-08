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





import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.adminHelpers import DEVS
from X.helpers.basic import edit_or_reply
from config import SUDO_USERS
from X.utils import extract_user

from .help import *


@Client.on_message(
    filters.command(["toxicity"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def ngejamet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**This command is forbidden to be used by my developers**"
        )
    xx = await edit_or_reply(message, "**WOW**")
    await asyncio.sleep(1.5)
    await xx.edit("**THE DICK OF AN ILLEGAL CHILD**")
    await asyncio.sleep(1.5)
    await xx.edit("**THE ONES BORN VILE AND UGLY**")
    await asyncio.sleep(1.5)
    await xx.edit("**WHAT ARE YOU DOING HERE DICK**")
    await asyncio.sleep(1.5)
    await xx.edit("**HERE I DON'T ACCEPT DESPITE PEOPLE LIKE YOU**")
    await asyncio.sleep(1.5)
    await xx.edit("**JUST PULL IT OUT THERE YOU PEPEK**")
    await asyncio.sleep(1.5)
    await xx.edit("**THERE'S NO POINT FOR YOU HERE YOU BITCH**")
    await asyncio.sleep(1.5)
    await xx.edit("**BYE DESPITE HUMAN WHO WAS BORN IN A POOR AND BAD FAMILY**")
    await asyncio.sleep(1.5)

@Client.on_message(
    filters.command(["idiot"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def ngejamet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**This command is forbidden to be used by my developers**"
        )
    xx = await edit_or_reply(message, "**WOOL**")
    await asyncio.sleep(1.5)
    await xx.edit("**WOW IDIOOTT**")
    await asyncio.sleep(1.5)
    await xx.edit("**YOU ARE AN IDIOT**")
    await asyncio.sleep(1.5)
    await xx.edit("**WHAT ARE YOU DOING HERE DICK**")
    await asyncio.sleep(1.5)
    await xx.edit("**HERE YOU DON'T ACCEPT RICH IDIOT PEOPLE WHO FUCK YOU**")
    await asyncio.sleep(1.5)
    await xx.edit("**JUST PULL IT OUT THERE, YOU SLUT**")
    await asyncio.sleep(1.5)
    await xx.edit("**THERE'S NO POINT FOR YOU HERE YOU BITCH**")
    await asyncio.sleep(1.5)
    await xx.edit("**THE DRUGS OF THE STUPID IDIOT CHILD IS UNIVERSAL**")
    await asyncio.sleep(1.5)


add_command_help(
    "toxic𝟷",
    [
        ["toxicity", "Tᴏ ɪᴜᴅɢᴇ ɪʟʟᴇɢɪᴛɪᴍᴀᴛᴇ ᴄʜɪʟᴅʀᴇɴ ʟɪᴋᴇ ʏᴏᴜ"],
        ["idiot", "Tᴏ Cᴏɴᴛᴀɪɴ ᴀɴ Iᴅɪᴏᴛ Kɪᴅ Lɪᴋᴇ ᴜ"],
    ]
  ) 
