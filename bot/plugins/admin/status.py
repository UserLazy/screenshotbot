from pyrogram import filters

from bot.config import Config
from bot.database import Database
from bot.screenshotbot import ScreenShotBot

db = Database()


@ScreenShotBot.on_message(
    filters.private & filters.command("status") & filters.user(Config.AUTH_USERS)
)
async def sts(c, m):
    total_users = await db.total_users_count()
    text = f"Total user(s) till date: {total_users}\n\n"
    text += f"Active users, today: {len(c.CHAT_FLOOD)}"
    await m.reply_text(text=text, quote=True)
