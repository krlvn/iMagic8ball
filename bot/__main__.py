import logging

from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.webhook.aiohttp_server import (
    SimpleRequestHandler,
    TokenBasedRequestHandler,
    setup_application,
)

from bot.handlers import commands
from bot.settings import *
from bot.languages import TEXT

async def set_commands(bot: Bot):
    await bot.set_my_commands([
        BotCommand(command='en', description='English'),
        BotCommand(command='fr', description='Français (French)'),
        BotCommand(command='es', description='Español (Spanish)'),
        BotCommand(command='ru', description='Русский (Russian)'),
    ])

async def on_startup_polling(dispatcher: Dispatcher, bot: Bot):
    await bot.delete_webhook(drop_pending_updates=True)

async def on_startup_webhook(dispatcher: Dispatcher, bot: Bot):
    await bot.set_webhook(
        url=f'''{WEBHOOK['URL']}{WEBHOOK['PATH']}''',
        drop_pending_updates=True,
        allowed_updates=dispatcher.resolve_used_update_types()
        )

def main() -> None:
    bot = Bot(token=TG_TOKEN, parse_mode='HTML')

    dp = Dispatcher()
    dp.include_router(commands.router)
    dp.startup.register(set_commands)

    try:
        if not WEBHOOK['URL']:
            dp.startup.register(on_startup_polling)
            dp.run_polling(bot, allowed_updates=dp.resolve_used_update_types())
        else:
            dp.startup.register(on_startup_webhook)

            app = web.Application()
            SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK['PATH'])
            setup_application(app, dp, bot=bot)
            web.run_app(app, host=SERVER['HOST'], port=SERVER['PORT'])
    finally:
        bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
