import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers import router


# MAIN ----------------------------------------------------------------
async def main() -> None:

    # BOT, DP ----------------------------------------------------------
    bot = Bot(
        token=os.getenv("BOT_TOKEN"),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )
    dp = Dispatcher()

    # ROUTERS ------------------------------------------------------

    dp.include_router(router)

    # ЗАПУСК БОТА --------------------------------------------------------------------
    try:

        print("Launch bot")
        # очищаем все предыдущие обновления, чтобы не получить ошибку при запуске
        await bot.delete_webhook(drop_pending_updates=True)
        # запускаем опрос на обновления для бота
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == "__main__":

    asyncio.run(main())

