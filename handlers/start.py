from aiogram import F, Router, types
from aiogram.filters import Command
from handlers.about_us import about_text
from db import queries

start_router = Router()





@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Our instagram", url="https://www.instagram.com/autobid.kg/"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="About us", callback_data="About"
                )
            ]
        ]
    )

    await message.answer(f"hi {message.from_user.first_name}", reply_markup=kb)


@start_router.callback_query(F.data == 'About')
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(about_text)
