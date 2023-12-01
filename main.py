import asyncio
from aiogram.types import BotCommand
import logging
from bot import bot, dp, scheduler
from handlers import (start_router, picture_router, myinfo_router,
                      shop_router, questions_router, products_router, subscribe_router)
from db.queries import (init_db, create_tables, populate_tables)
from handlers.delayed_answer import set_mailing


async def on_startup(dispatcher):
    init_db()
    create_tables()
    populate_tables()

    scheduler.add_job(set_mailing, 'interval', seconds=3, id='send_mailing', args=(dp,))
    scheduler.start()


async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="Start"),
        BotCommand(command="picture", description="Show picture"),
        BotCommand(command="myinfo", description="My information"),
        BotCommand(command="shop", description="Shop"),
        BotCommand(command="questions", description="Small survey about your car preferences"),
        BotCommand(command="show_products", description="List of products"),
        BotCommand(command="subscribe", description="Subscribe for our mailing")
    ])

    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(picture_router)
    dp.include_router(shop_router)
    dp.include_router(questions_router)
    dp.include_router(products_router)
    dp.include_router(subscribe_router)

    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
