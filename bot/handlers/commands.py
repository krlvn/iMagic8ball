from random import randint

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


@router.message()
async def dialog_activity(message: Message):
    user = await get_or_create_user(message.from_user.id,
                                    message.from_user.language_code)

    if user.language not in ['en','fr','es','ru']:
        user.language = 'en'

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=TEXT[user.language.upper()][2],
                                 callback_data='once_again'),
        ],
    ])

    # TODO: загружаем и отправляем стикер либо фото
    photo_file = 'img/' + user.language + '/' + str(randint(1,20)) + '.png'
    # sticker = open(photo_file, 'rb')
    # bot.send_sticker(message.from_user.id, sticker,
    #                  reply_markup=keyboard)

    # image = types.InputFile(f'img/{language}/{randint(1,20)}.png')
    # await bot.send_photo(message.from_user.id,
    #                        photo=image,
    #                        reply_markup=keyboard)

    await message.answer(photo_file,
                         reply_markup=keyboard)

@router.callback_query(text='once_again')
async def dialog_activity(callback: CallbackQuery):
    user = await get_or_create_user(callback.from_user.id,
                                    callback.from_user.language_code)

    if user.language not in ['en','fr','es','ru']:
        user.language = 'en'

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=TEXT[user.language.upper()][2],
                                 callback_data='once_again'),
        ],
    ])

    # TODO: загружаем и отправляем стикер либо фото
    photo_file = 'img/' + user.language + '/' + str(randint(1,20)) + '.png'
    # sticker = open(photo_file, 'rb')
    # bot.send_sticker(message.from_user.id, sticker,
    #                  reply_markup=keyboard)

    # image = types.InputFile(f'img/{language}/{randint(1,20)}.png')
    # await bot.send_photo(message.from_user.id,
    #                        photo=image,
    #                        reply_markup=keyboard)

    await callback.message.answer(photo_file,
                         reply_markup=keyboard)
