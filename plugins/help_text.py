#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
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
from seedr import SeedrAPI
import re
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
seedr = SeedrAPI(email="masoudakhoondi1@gmail.com", password="12345678")

# Def Get Info

def human_readable_size(size, decimal_places=3):

    for unit in ['B','KiB','MiB','GiB','TiB']:

        if size < 1024.0:

            break

        size /= 1024.0

    return f"{size:.{decimal_places}f}{unit}"
def Get_Folders_ID():

    num = 0 

    output = ''

    Get_Drives = seedr.get_drive()

    #foldercount = len(Get_Drives["folders"])

    folders = Get_Drives["folders"]

    for i in folders:

        idd = folders[num]["id"]

        name = folders[num]["name"]

        size = human_readable_size(folders[num]["size"])

        out = "نام فایل :\n{} \nدانلود فولدر : /get_{} \nحجم فولدر : {} \n\n++++++++++++++\n\n".format(name,idd,size)

        num = num+1

        output = str(out + output)

    space_used = human_readable_size(Get_Drives["space_used"])

    space_max = human_readable_size(Get_Drives["space_max"])

    siz = "کل فضای شما : {} \nفضای مصرفی شما : {}".format(space_max,space_used)

    output = str(output + siz)

    return output
def Get_Files_ID(ID):

    num = 0 

    output = []

    Get_Folder = seedr.get_folder(ID)

    #foldercount = len(Get_Drives["folders"])

    filesss = Get_Folder["files"]

    for i in filesss:

        idd = filesss[num]["folder_file_id"]

        name = filesss[num]["name"]

        sizz = human_readable_size(filesss[num]["size"])

        out = {"id" : idd , "name" : name , "size" : sizz}

        num = num+1

        output.append(out)

        

    return output
def Get_Link(ID):
    Get_File_link = seedr.get_file(ID)["url"]
    return Get_File_link
def resualt_text(ID_File):
    All = Get_Files_ID(ID_File)
    num = 0 
    output = ''
    for i in All:
        name = All[num]["name"]
        ids =  All[num]["id"]
        size =  All[num]["size"]
        Link = Get_Link(ids)
        text = "نام فایل : {} \n📥 لینک دانلود : \n{}\nحجم فایل : {}\nدانلود فایل : /download_{}\n\n++++++++++++++\n\n".format(name,Link,size,ids)
        num = num+1
        output = output + str(text)
    return output
def Add_TR(Magnet):

    output = seedr.add_torrent(Magnet)

    if output["result"] == 'not_enough_space_added_to_wishlist':

        title = output['wt']["title"]

        res = {'stat':'not_enough_space_added_to_wishlist',"name":title} 

    elif output["code"] == 200 :

        title = output["title"]

        res = {'stat':'ok',"name": title}

    else :

        res = {'stat':'no',"name": ""}

    

    return res

@Clinton.on_message(filters.command("showfile"))
async def getfile_command(bot, message):
    textt = Get_Folders_ID()
    await message.reply_text(textt)

@Clinton.on_message(filters.private & filters.regex(pattern=".*magnet.*"))
async def add_file(bot, message):
    await message.reply_text('فایل شما برای تبدیل ثبت شد ... تا زمان دانلود میتوانید از بخش /showfile پیگیری کنید')
    Add_TR(message.text)
    stat = Add_TR['stat']
    if stat == 'ok':
        name = Add_TR['name']
        await message.reply_text("فایل با نام ")
        await message.reply_text("فایل با نام "+'{}'+" ثبت شد ".format(name))
    elif stat == 'not_enough_space_added_to_wishlist':
        await message.reply_text("فضای کافی ندارید")
    else:
        await message.reply_text("خطایی رخ داده است ")


@Clinton.on_message(filters.private & filters.regex(pattern=".*get.*"))
async def get_file_info(bot, message):
    await message.reply_text('لطفا کمی صبر کنید ...')
    pattern_link = re.compile(r'^\/get_(.*)')
    matches_link = pattern_link.search(str(message.text))
    p_id = matches_link.group(1)
    texttt = resualt_text(p_id)
    await message.reply_text(texttt)


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
