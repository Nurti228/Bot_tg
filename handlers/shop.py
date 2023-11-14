from aiogram import F, Router, types
from aiogram.filters import Command

shop_router = Router()


@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Cars")
            ],
            [
                types.KeyboardButton(text="Services")
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Choose what you want", reply_markup=kb)

    @shop_router.message(F.text == "Cars")
    async def show_cars(message: types.Message):
        kb_back = types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(text="Back to Main Menu")
                ]
            ],
            resize_keyboard=True
        )
        await message.answer("Cars in our garage", reply_markup=kb_back)

    @shop_router.message(F.text == "Services")
    async def show_cars(message: types.Message):
        kb_back = types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(text="Back to Main Menu")
                ]
            ],
            resize_keyboard=True
        )
        await message.answer("Services that we provide", reply_markup=kb_back)


@shop_router.message(F.text == "Back to Main Menu")
async def back_to_main_menu(message: types.Message):
    kb_main_menu = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Cars")
            ],
            [
                types.KeyboardButton(text="Services")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Back to main menu", reply_markup=kb_main_menu)
