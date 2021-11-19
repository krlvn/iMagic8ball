#!/usr/bin/env python
# -*- coding: utf8 -*-

################### Это телеграм-бот magic8ball

import sys
import random
import telebot
from telebot import types

telegram_bot = telebot.TeleBot('1876177016:AAE7YO3RkyKjvWzftIR2LHluT0i4RFexrio')

def keybord_buttons(message):
      keyboard = types.InlineKeyboardMarkup();
      key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
      keyboard.add(key_yes); #добавляем кнопку в клавиатуру
      key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
      keyboard.add(key_no);

      mm = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True,)
      button1 = types.KeyboardButton("Узнать ответ")

      mm.row(button1)

      return mm
      
      
@telegram_bot.message_handler(commands=['start'])
def get_commands(message):
    telegram_bot.send_message(message.from_user.id, text='Привет, я бот-предсказатель. Мысленно задай вопрос и нажми кнопку Встряхнуть', reply_markup=keybord_buttons(message))
       
@telegram_bot.message_handler(content_types=['text'])
def get_text_messages(message):
    photo_file = 'ball_' + str(random.randint(1,20)) + '.png'
    photo = open(photo_file, 'rb')
    telegram_bot.send_photo(message.chat.id, photo)
    print(message.from_user.id)
    print(message.from_user.username)
    print(message.from_user.first_name)
    print(message.from_user.last_name)
    print(message.from_user.is_bot)
    print(message.from_user.language_code)

    
 


telegram_bot.polling(none_stop=True, interval=0)



















##from datetime import datetime
##import vk_api
##import requests
##import json
##import re
##import configparser
##import sys
##import time
##import random
##import urllib
##import wget # Скачивание файла из инета
##import telebot
##from telebot import types
##
##telegram_bot = telebot.TeleBot('1876177016:AAE7YO3RkyKjvWzftIR2LHluT0i4RFexrio')
##
##lang = 'ru'
##
##def keybord_buttons(message):
##      keyboard = types.InlineKeyboardMarkup();
##      key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
##      keyboard.add(key_yes); #добавляем кнопку в клавиатуру
##      key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
##      keyboard.add(key_no);
##
##      mm = types.ReplyKeyboardMarkup(row_width=1)
##      button1 = types.KeyboardButton("Встряхнуть")
##      if lang == 'ru':
##          button2 = types.KeyboardButton("English")
##      else:
##          button2 = types.KeyboardButton("Русский")
##      
##      mm.add(button1)
##
##      return mm
##      
##      
##@telegram_bot.message_handler(commands=['start'])
##def get_commands(message):
##    telegram_bot.send_message(message.from_user.id, text='Привет, я бот-предсказатель. Мысленно задай вопрос и нажми кнопку Встряхнуть', reply_markup=keybord_buttons(message))
##       
##@telegram_bot.message_handler(content_types=['text'])
##def get_text_messages(message):
##
##    global lang
##
##    answers_ru = [
##        'Бесспорно',
##        'Предрешено',
##        'Никаких сомнений',
##        'Определённо да',
##        'Можешь быть уверен в этом',
##        'Мне кажется — «да»',
##        'Вероятнее всего',
##        'Хорошие перспективы',
##        'Знаки говорят — «да»',
##        'Да',
##        'Пока не ясно, попробуй снова',
##        'Спроси позже',
##        'Лучше не рассказывать',
##        'Сейчас нельзя предсказать',
##        'Сконцентрируйся и спроси опять',
##        'Даже не думай',
##        'Мой ответ — «нет»',
##        'По моим данным — «нет»',
##        'Перспективы не очень хорошие',
##        'Весьма сомнительно'
##    ]
##
##
##    answers_en = [
##        'It is certain',
##        'It is decidedly so',
##        'Without a doubt',
##        'Yes — definitely',
##        'You may rely on it',
##        'As I see it, yes',
##        'Most likely',
##        'Outlook good',
##        'Signs point to yes',
##        'Yes',
##        'Reply hazy, try again',
##        'Ask again later',
##        'Better not tell you now',
##        'Cannot predict now',
##        'Concentrate and ask again',
##        'Don’t count on it',
##        'My reply is no',
##        'My sources say no',
##        'Outlook not so good',
##        'Very doubtful'
##    ]
##                      
##    if message.text == "Встряхнуть":
##        if lang == 'ru':
##            answer = random.choice(answers_ru)
##        else:
##            answer = random.choice(answers_en)
##
##        photo_file = 'ball_' + str(random.randint(1,20)) + '.png'
##        photo = open(photo_file, 'rb')
##        telegram_bot.send_photo(message.chat.id, photo)
##
####        telegram_bot.send_message(message.chat.id, answer)
##        keybord_buttons(message)
##    elif message.text == 'English':
##        lang = 'en'
##        telegram_bot.send_message(message.chat.id, "English")
##        keybord_buttons(message)
##    elif message.text == "Русский":
##        lang = 'ru'
##        telegram_bot.send_message(message.chat.id, "Русский")
##
##    
## 
##
##
##telegram_bot.polling(none_stop=True, interval=0)
