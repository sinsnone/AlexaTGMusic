# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali
# Harshit Sharma


import asyncio
from os import path

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message, Voice
from youtube_search import YoutubeSearch

import Alexa
from Alexa import (
    BOT_USERNAME,
    DURATION_LIMIT,
    DURATION_LIMIT_MIN,
    MUSIC_BOT_NAME,
    app,
    db_mem,
)
from Alexa.Core.PyTgCalls.Converter import convert
from Alexa.Core.PyTgCalls.Downloader import download
from Alexa.Core.PyTgCalls.Tgdownloader import telegram_download
from Alexa.Database import get_active_video_chats, get_video_limit, is_active_video_chat
from Alexa.Decorators.assistant import AssistantAdd
from Alexa.Decorators.checker import checker
from Alexa.Decorators.logger import logging
from Alexa.Inline import (
    livestream_markup,
    playlist_markup,
    search_markup,
    search_markup2,
    url_markup,
    url_markup2,
)
from Alexa.Utilities.changers import seconds_to_min, time_to_seconds
from Alexa.Utilities.chat import specialfont_to_normal
from Alexa.Utilities.command import commandpro
from Alexa.Utilities.stream import start_stream, start_stream_audio
from Alexa.Utilities.theme import check_theme
from Alexa.Utilities.thumbnails import gen_thumb
from Alexa.Utilities.url import get_url
from Alexa.Utilities.videostream import start_stream_video
from Alexa.Utilities.youtube import (
    get_yt_info_id,
    get_yt_info_query,
    get_yt_info_query_slider,
)

from Alexa.Utilities.func import mplay_stream, vplay_stream


@app.on_message(
    commandpro(["/p", "Play", "/play", f"/play@{BOT_USERNAME}"])
)
@checker
@logging
@AssistantAdd
async def mplayaa(_, message: Message):
    await message.delete()
    if message.chat.id not in db_mem:
        db_mem[message.chat.id] = {}
    if message.sender_chat:
        return await message.reply_text(
            "**ʏᴏᴜ'ʀᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ ɢʀᴏᴜᴘ** 😜....\n**ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs**.... 😜"
        )
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    video = (
        (message.reply_to_message.video or message.reply_to_message.document)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        mystic = await message.reply_text("🔄 ᴘʀᴏᴄᴇssɪɴɢ ᴀᴜᴅɪᴏ....")
        try:
            read = db_mem[message.chat.id]["live_check"]
            if read:
                return await mystic.edit(
                    "Live Streaming Playing...Stop it to play music"
                )
            else:
                pass
        except:
            pass
        if audio.file_size > 1073741824:
            return await mystic.edit_text("ᴀᴜᴅɪᴏ ғɪʟᴇ sɪᴢᴇ sʜᴏᴜʟᴅ ʙᴇ ʟᴇss ᴛʜᴀɴ 𝟷𝟻𝟶 ᴍʙ")
        duration_min = seconds_to_min(audio.duration)
        duration_sec = audio.duration
        if (audio.duration) > DURATION_LIMIT:
            return await mystic.edit_text(
                f"**ᴅᴜʀᴀᴛɪᴏɴ ʟɪᴍɪᴛ ᴇxᴄᴇᴇᴅᴇᴅ**\n\n**ᴀʟʟᴏᴡᴇᴅ ᴅᴜʀᴀᴛɪᴏɴ: **{DURATION_LIMIT_MIN} ᴍɪɴᴜᴛᴇs\n**ʀᴇᴄᴇɪᴠᴇᴅ ᴅᴜʀᴀᴛɪᴏɴ:** {duration_min} minute(s)"
            )
        file_name = (
            audio.file_unique_id
            + "."
            + (
                (audio.file_name.split(".")[-1])
                if (not isinstance(audio, Voice))
                else "ogg"
            )
        )
        file_name = path.join(path.realpath("downloads"), file_name)
        file = await convert(
            (await message.reply_to_message.download(file_name))
            if (not path.isfile(file_name))
            else file_name,
        )
        return await start_stream_audio(
            message,
            file,
            "smex1",
            "Given Audio Via Telegram",
            duration_min,
            duration_sec,
            mystic,
        )
    elif video:
        return await message.reply_text(
            "ᴜsᴇ `/play` ᴏʀ `/vplay` ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴘʟᴀʏ ᴀᴜᴅɪᴏ ᴏʀ ᴠɪᴅᴇᴏ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ..."
        )
    elif url:
        mystic = await message.reply_text("🔄 ᴘʀᴏᴄᴇssɪɴɢ ᴜʀʟ....")
        if not message.reply_to_message:
            query = message.text.split(None, 1)[1]
        else:
            query = message.reply_to_message.text
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        await mystic.delete()
        MusicData = f"MusicStream {videoid}|{duration_min}|{message.from_user.id}"
        return await mplay_stream(message, MusicData)
    else:
        if len(message.command) < 2:
            buttons = playlist_markup(
                message.from_user.first_name, message.from_user.id, "abcd"
            )
            await message.reply_photo(
                photo="Utils/Playlist.jpg",
                caption=(
                    "**ᴜsᴀɢᴇ:** `/play` [ᴍᴜsɪᴄ ɴᴀᴍᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ ғɪʟᴇ]\n\nɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘʟᴀʏ ᴘʟᴀʏʟɪsᴛs sᴇʟᴇᴄᴛ ᴛʜᴇ ᴏɴᴇ ғʀᴏᴍ ʙᴇʟᴏᴡ..."
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            return
        mystic = await message.reply_text("**sᴇᴀʀᴄʜɪɴɢ...**")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        await mystic.delete()
        MusicData = f"MusicStream {videoid}|{duration_min}|{message.from_user.id}"
        return await mplay_stream(message, MusicData)


@app.on_message(
    commandpro(["/v", "/vplay", "vplay", f"/vplay@{BOT_USERNAME}"])
)
@checker
@logging
@AssistantAdd
async def vplayaaa(_, message: Message):
    await message.delete()
    if message.chat.id not in db_mem:
        db_mem[message.chat.id] = {}
    if message.sender_chat:
        return await message.reply_text(
            "**ʏᴏᴜ'ʀᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ ɢʀᴏᴜᴘ**...😜\n**ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs**...😜"
        )
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    video = (
        (message.reply_to_message.video or message.reply_to_message.document)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        return await message.reply_text(
            "ᴜsᴇ `/play` ᴏʀ `/vplay` ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴘʟᴀʏ ᴀᴜᴅɪᴏ ᴏʀ ᴠɪᴅᴇᴏ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ..."
        )
    elif video:
        limit = await get_video_limit(141414)
        if not limit:
            return await message.reply_text(
                "**ɴᴏ ʟɪᴍɪᴛ ᴅᴇғɪɴᴇᴅ ғᴏʀ ᴠɪᴅᴇᴏ ᴄᴀʟʟs**\n\nsᴇᴛ ᴀ ʟɪᴍɪᴛ ғᴏʀ ɴᴜᴍʙᴇʀ ᴏғ ᴍᴀxɪᴍᴜᴍ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴀʟʟᴏᴡᴇᴅ ᴏɴ ʙᴏᴛ ʙʏ `/set_video_limit` [sᴜᴅᴏ ᴜsᴇʀs ᴏɴʟʏ]"
            )
        count = len(await get_active_video_chats())
        if int(count) == int(limit):
            if await is_active_video_chat(message.chat.id):
                pass
            else:
                return await message.reply_text(
                    "**sᴏʀʀʏ ʙᴏᴛ ᴏɴʟʏ ᴀʟʟᴏᴡs ʟɪᴍɪᴛᴇᴅ ɴᴜᴍʙᴇʀ ᴏғ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴅᴜᴇ ᴛᴏ ᴄᴘᴜ ᴏᴠᴇʀʟᴏᴀᴅ ɪssᴜᴇs. ᴍᴀɴʏ ᴏᴛʜᴇʀ ᴄʜᴀᴛs ᴀʀᴇ ᴜsɪɴɢ ᴠɪᴅᴇᴏ ᴄᴀʟʟ ʀɪɢʜᴛ ɴᴏᴡ. ᴛʀʏ sᴡɪᴛᴄʜɪɴɢ ᴛᴏ ᴀᴜᴅɪᴏ ᴏʀ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ**..."
                )
        mystic = await message.reply_text("🔄 ᴘʀᴏᴄᴇssɪɴɢ ᴠɪᴅᴇᴏ...")
        try:
            read = db_mem[message.chat.id]["live_check"]
            if read:
                return await mystic.edit("ʟɪᴠᴇs sᴛʀᴇᴀᴍɪɴɢ.../nsᴛᴏᴘ ɪᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ...")
            else:
                pass
        except:
            pass
        file = await telegram_download(message, mystic)
        return await start_stream_video(
            message,
            file,
            "Given Video Via Telegram",
            mystic,
        )
    elif url:
        mystic = await message.reply_text("🔄 ᴘʀᴏᴄᴇssɪɴɢ ᴜʀʟ...")
        if not message.reply_to_message:
            query = message.text.split(None, 1)[1]
        else:
            query = message.reply_to_message.text
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)

        VideoData = f"ᴄʜᴏᴏsᴇ {videoid}|{duration_min}|{message.from_user.id}"
        return await vplay_stream(message, VideoData, mystic)
    else:
        if len(message.command) < 2:
            buttons = playlist_markup(
                message.from_user.first_name, message.from_user.id, "abcd"
            )
            await message.reply_photo(
                photo="Utils/Playlist.jpg",
                caption=(
                    "**ᴜsᴀɢᴇ:** `/vplay` [ᴍᴜsɪᴄ ɴᴀᴍᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ]\n\nɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘʟᴀʏ ᴘʟᴀʏʟɪsᴛs sᴇʟᴇᴄᴛ ᴛʜᴇ ᴏɴᴇ ғʀᴏᴍ ʙᴇʟᴏᴡ..."
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            return
        mystic = await message.reply_text("🔄 ᴘʀᴏᴄᴇssɪɴɢ...")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        VideoData = f"ᴄʜᴏᴏsᴇ {videoid}|{duration_min}|{message.from_user.id}"
        return await vplay_stream(message, VideoData, mystic)
