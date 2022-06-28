#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modified By > @DC4_WARRIOR
import asyncio
from pyrogram import filters
from pyrogram import Client as Clinton
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.dl_button import ddl_call_back
from plugins.seed import *
from plugins.buttons import *

@Clinton.on_callback_query(filters.regex('^X0$'))
async def delt(bot, update):
          await update.message.delete(True)


@Clinton.on_callback_query()
async def button(bot, update):

    cb_data = update.data
    if "|" in cb_data:
        await youtube_dl_call_back(bot, update)
    elif "ref" in cb_data:
        
        texttt = active()
        await update.message.delete(True)
        if texttt == "noActiveTorrents":
            texttts = folders()
            print(texttts)
            await bot.send_message(
                chat_id=update.chat.id,
                text=texttts, 
                #parse_mode="html",
                #reply_markup=Button.BUTTONS01
            )
            
        else:    
          print(texttt)
          await bot.send_message(
                chat_id=update.chat.id,
                text=texttts, 
                #parse_mode="html",
                reply_markup=Button.refresh
          )
         
            
    elif "=" in cb_data:
        await ddl_call_back(bot, update)
