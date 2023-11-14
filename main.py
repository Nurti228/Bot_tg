import asyncio
from aiogram.types import BotCommand
import logging

from bot import bot, dp

from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.picture import picture_router
from handlers.shop import shop_router


async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="Start"),
        BotCommand(command="picture", description="Show picture"),
        BotCommand(command="myinfo", description="My information"),
        BotCommand(command="shop", description="Shop"),
    ])

    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(picture_router)
    dp.include_router(shop_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
