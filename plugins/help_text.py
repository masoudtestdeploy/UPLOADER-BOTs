#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
from plugins.buttons import *
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
# the Strings used for this "thing"
from translation import Translation

from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as Clinton
logging.getLogger("pyrogram").setLevel(logging.WARNING)
import re
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.seed import *
from plugins.buttons import *
# Def Get Info


@Clinton.on_message(filters.private & filters.command(["account"]))
async def accounyt(bot, update):
    # logger.info(update)
    texttt =  account()
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=texttt,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Clinton.on_message(filters.private & filters.command(["active"]))
async def activye(bot, update):
    # logger.info(update)
    texttt = active()
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=texttt,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=Button.refresh
    )
    
@Clinton.on_message(filters.private & filters.regex(pattern=".*magnet:?.*"))
async def magnety(bot, update):
    # logger.info(update)
    texttt = addTorrent(magnetLink=update.text)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=texttt,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
    
@Clinton.on_message(filters.private & filters.regex(pattern=".*delete.*"))
async def deleteFoldery(bot, update):
    # logger.info(update)
    pattern_link = re.compile(r'^\/delete_(.*)')
    matches_link = pattern_link.search(str(update.text))
    p_id = matches_link.group(1)
    texttt = deleteFolder(p_id)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=texttt,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
    

@Clinton.on_message(filters.private & filters.command(["folder"]))
async def foldexrsy(bot, update): 
    texttts = folders()
    #print(texttts)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=texttts,
        #parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Clinton.on_message(filters.private & filters.command(["wishlist"]))
async def foldersy(bot, update): 
    texttt = wishlist()
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=texttt,
        #parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )    
@Clinton.on_message(filters.private & filters.regex(pattern=".*getFiles.*"))
async def getFilesy(bot, update):
    # logger.info(update)
    pattern_link = re.compile(r'^\/getFiles_(.*)')
    matches_link = pattern_link.search(str(update.text))
    p_id = matches_link.group(1)
    texttt = getFiles(p_id)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=texttt,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
    
@Clinton.on_message(filters.private & filters.regex(pattern=".*fileLink.*"))
async def getLinky(bot, update):
    # logger.info(update)
    pattern_link = re.compile(r'^\/fileLink_(.*)')
    matches_link = pattern_link.search(str(update.text))
    p_id = matches_link.group(1)
    texttt = getLink(p_id)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=texttt,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
    
    
@Clinton.on_message(filters.private & filters.regex(pattern=".*remove.*"))
async def getLinkfg(bot, update):
    # logger.info(update)
    pattern_link = re.compile(r'^\/remove_(.*)')
    matches_link = pattern_link.search(str(update.text))
    p_id = matches_link.group(1)
    texttt = removeFile(p_id)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=texttt,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
    
@Clinton.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Clinton.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "کانال ما ⚡", url="https://t.me/kenzomoviee"
                    ),
                    InlineKeyboardButton("کانال پشتیبان 👨🏻‍💻", url="https://t.me/kenzomovie"),
                ],
                [InlineKeyboardButton("برنامه نویس 👨‍⚖️", url="https://t.me/masoudartwork")],
            ]
        ),
        reply_to_message_id=update.message_id
    )
