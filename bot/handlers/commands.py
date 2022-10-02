# from random import choice as rc

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery, ContentType, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command

# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup

from bot.db.requests import *
from bot.languages import TEXT


router = Router()

@router.message(Command(commands=['start','en','fr','es','ru']))
async def cmd_start(message: Message, command: Command):
    if command.command == 'start':
        user = await get_or_create_user(message.from_user.id,
                                        message.from_user.language_code)
    else:
        user = await update_or_create_user(message.from_user.id,
                                        language = command.command)

    if user.language not in ['en','fr','es','ru']:
        user.language = 'en'

    # TODO: Отправляем стикер и текст или фото с подписью.
    await message.answer(TEXT[user.language.upper()][1])
