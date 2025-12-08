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

from pyrogram import filters, Client
from pyrogram.types import Message

from config import SUDO_USERS
from X.helpers.aiohttp_helper import AioHttp
from .help import *


@Client.on_message(
    filters.command(["unsplash", "pic"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def unsplash_pictures(bot: Client, message: Message):
    cmd = message.command

    if len(cmd) > 1 and isinstance(cmd[1], str):
        keyword = cmd[1]

        if len(cmd) > 2 and int(cmd[2]) < 10:
            await message.edit("```Getting Pictures```")
            count = int(cmd[2])
            images = []
            while len(images) is not count:
                img = await AioHttp().get_url(
                    f"https://source.unsplash.com/1600x900/?{keyword}"
                )
                if img not in images:
                    images.append(img)

            for img in images:
                await bot.send_photo(message.chat.id, str(img))

            await message.delete()
            return
        else:
            await message.edit("```Getting Picture```")
            img = await AioHttp().get_url(
                f"https://source.unsplash.com/1600x900/?{keyword}"
            )
            await asyncio.gather(
                message.delete(), 
                bot.send_photo(message.chat.id, str(img))
            )



add_command_help(
    "unsplash",
    [
        [".unsplash ᴏʀ .pic", "Sᴇɴᴅ ʀᴀɴᴅᴏᴍ ᴘɪᴄ ᴏғ ᴋᴇʏᴡᴏʀᴅ ғɪʀꜱᴛ ᴀʀɢᴜᴍᴇɴᴛ."],
    ],
)
