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
import re

from pyrogram import filters, Client
from pyrogram.errors import MessageNotModified
from pyrogram.types import Message
from config import SUDO_USERS

from .help import *

bad_words = ["nigga", "nigger", "coon", "retard", "fuck", "motherfucker"]

vulgar_filter = True


def switch():
    global vulgar_filter
    vulgar_filter = not vulgar_filter
    return vulgar_filter



@Client.on_message(
    filters.command(["vulgar"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def toggle(bot: Client, message: Message):
    c = switch()
    await message.edit("`Vulgar Enabled`" if c else "`Vulgar Disabled`")
    await asyncio.sleep(3)
    await message.delete()


@Client.on_message(~filters.regex(r"^\.\w*") & filters.me & ~filters.media, group=10)
async def i_am_not_allowed_to_say_this(bot: Client, message: Message):
    if vulgar_filter:
        try:
            txt = None
            if message.caption:
                txt = message.caption
            elif message.text:
                txt = message.text

            for word in bad_words:
                try:
                    txt = re.sub(word, "bruh", txt, flags=re.IGNORECASE)
                except Exception as e:
                    print(f"{e}")

            if message.caption:
                if txt != message.caption:
                    await message.edit_caption(txt)

            elif message.text:
                if txt != message.text:
                    await message.edit(txt)
        except MessageNotModified:
            return


add_command_help(
    "vulgar",
    [
        [".vulgar", "Tᴏɢɢʟᴇꜱ ʙᴀᴅ ᴡᴏʀᴅ ғɪʟᴛᴇʀɪɴɢ ᴏɴ ᴀɴᴅ ᴏғғ."],
    ],
)
