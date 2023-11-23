from aiogram import Router, types
from aiogram.filters import Command
from db.queries import get_products

products_router = Router()


@products_router.message(Command('show_products'))
async def show_answer(message: types.Message):
    product = get_products()
    product_str = '\n'.join(map(str, product))
    await message.answer(product_str)
