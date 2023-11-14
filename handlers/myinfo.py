from aiogram import Router, types
from aiogram.filters import Command

myinfo_router = Router()


@myinfo_router.message(Command("myinfo"))
async def echo(message: types.Message):
    print(message)
    await message.answer(f" Your name is: {message.from_user.first_name}, Your id is: {message.from_user.id}")
