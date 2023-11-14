from aiogram import Router, types
from aiogram.filters import Command
from pathlib import Path
from random import choice

picture_router = Router()


@picture_router.message(Command("picture"))
async def pic(message: types.Message):
    ca = []
    p = Path('images')
    for c in p.iterdir():
        ca.append(c)
    file = types.FSInputFile(choice(ca))
    await message.answer_photo(
        photo=file,
    )
