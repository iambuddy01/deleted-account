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




from asyncio import gather
from random import choice

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from config import SUDO_USERS
from X.helpers.basic import edit_or_reply
from X.helpers.PyroHelpers import ReplyCheck

from .help import *


@Client.on_message(
    filters.command(["asupan", "ptl"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def asupan_cmd(client: Client, message: Message):
    X = await edit_or_reply(message, "`Wait More Search for Lu's Intake...`")
    await gather(
        X.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "have it", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

@Client.on_message(
    filters.command(["bkp"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def bkp_cmd(client: Client, message: Message):
    X = await edit_or_reply(message, "`Wait More Find Bra Material For Lu..`")
    await gather(
        X.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    bkp.video.file_id
                    async for bkp in client.search_messages(
                        "bokepX", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


# WARNING PORNO VIDEO THIS !!!



@Client.on_message(
    filters.command(["ayang"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Is...`")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Unfortunately [{pop}](tg://user?id={ah}) 💝",
    )

    await yanto.delete()


@Client.on_message(
    filters.command(["ppcp", "couple"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def ppcp(client, message):
    yanto = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Couple here is some couples pics",
    )

    await yanto.delete()


@Client.on_message(
    filters.command(["ppanime"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def ppanime(client, message):
    yanto = await message.reply("🔎 `Search PP Anime...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Wibu here is some couples pics",
    )

    await yanto.delete()


add_command_help(
    "asupan",
    [
        [
            f"asupan atau {cmd}ptl",
            "Tᴏ ꜱᴇɴᴅ ɪɴᴛᴀᴋᴇ ᴠɪᴅᴇᴏꜱ ʀᴀɴᴅᴏᴍʟʏ.",
        ],
        [
            f"ayang {cmd}",
            "Tᴏ ꜱᴇᴀʀᴄʜ ғᴏʀ ʀᴀɴᴅᴏᴍ ᴘʜᴏᴛᴏꜱ ᴏғ Aʏᴀɴɢ.",
        ],
        [
            f"ppcp atau {cmd}couple",
            "Tᴏ Sᴇᴀʀᴄʜ ғᴏʀ Pᴘ Cᴏᴜᴘʟᴇꜱ Rᴀɴᴅᴏᴍʟʏ.",
        ],
        [
            f"ppanime {cmd}",
            "Tᴏ ꜱᴇᴀʀᴄʜ ғᴏʀ ᴀɴɪᴍᴇ ᴘᴘ ʀᴀɴᴅᴏᴍʟʏ.",
        ]
    ],
)
