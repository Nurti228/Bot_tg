from aiogram import Router, types
from aiogram.filters import Command
from db.queries import subscribe_user

subscribe_router = Router()


@subscribe_router.message(Command("subscribe"))
async def sub_user(message: types.Message):
    user_id = str(message.from_user.id)
    user_name = message.from_user.full_name
    subscribe_user(user_id, user_name)
    await message.answer("You successfully subscribed!")
