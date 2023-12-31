import asyncio
import logging

from aiogram import Bot, Dispatcher
from keyboards.set_menu import set_main_menu
from config.config import Config, load_config
from handlers import admin_handlers, user_handlers, private_user_handlers

# Инициализация логгера
logger = logging.getLogger(__name__)


async def main() -> None:
    # Конфигурация логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s'
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')


    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Настраиваем кнопку Menu
    await set_main_menu(bot)

    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(private_user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())