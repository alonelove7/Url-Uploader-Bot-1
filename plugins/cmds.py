#https://github.com/PredatorHackerzZ/RENAMER-BOT


import os
import sqlite3
import logging
import pyrogram

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("WEBHOOK", False)):

    from sample_config import Config
else:
    from config import Config

from pyrogram import filters
from scripts import Scripted
from pyrogram import Client as Clinton
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Clinton.on_message(
    filters.command(["start"]) &
    filters.private &
    filters.user(Config.AUTH_USERS) if Config.PRIVATE else None
)
async def start(bot, update):
    await update.reply_text(
        text=Scripted.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Scripted.START_BUTTONS
    )




