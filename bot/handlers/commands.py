# from random import choice as rc

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery, ContentType, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command

# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup

router = Router()

@router.message(Command(commands='start'))
async def cmd_rules(message: Message):
    await message.answer('<b>Hello bot!</b>')
