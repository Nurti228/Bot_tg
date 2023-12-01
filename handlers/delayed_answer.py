from aiogram import Router, Dispatcher
from db.queries import get_user_id
import asyncio

delayed_answer_router = Router()


async def send_mail():
    from bot import bot, dp
    users = get_user_id()
    for user in users:
        await bot.send_message(user[1], "Update")


async def set_mailing(dp: Dispatcher):
    await asyncio.sleep(5)
    await send_mail()
