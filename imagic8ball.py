#!/usr/bin/env python
# -*- coding: utf8 -*-

import telebot
import sqlite3
from random import randint
from settings import token, texts


# Connect (or create) DB sqlight3 for save user's language
try:
    sqlite_connection = sqlite3.connect('db.sqlite3')                           
    cursor = sqlite_connection.cursor()

    sqlite_create_table_query = "CREATE TABLE user_language (id INTEGER PRIMARY KEY, language TEXT NOT NULL)"          
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print('Error : ', error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()


# Connect telegram
bot = telebot.TeleBot(token)


# Create menu with commands
bot.set_my_commands([
    telebot.types.BotCommand('/en', 'English'),
    telebot.types.BotCommand('/fr', 'Français (French)'),
    telebot.types.BotCommand('/es', 'Español (Spanish)'),
    telebot.types.BotCommand('/ru', 'Русский (Russian)')
])


def get_user_language(user_id,tg_lang):
    # Connect (or create) DB sqlight3 for save user's language
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
    except sqlite3.Error as error:
        print('Error : ', error)
        
    # Get user language from DB
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT language FROM user_language WHERE id = ? LIMIT 0, 1", (user_id,))
    record = cursor.fetchone()
    cursor.close()        

    if record != None:
        # Get user language from DB
        language = record[0]
    else:

        # Get language of telegram
        language = 'en'
        if str(tg_lang) in ['en','fr','es','ru']:
            language = str(tg_lang)
             
        # Add user to DB
        cursor = sqlite_connection.cursor()
        cursor.execute("INSERT INTO user_language (id, language) VALUES (?, ?)", (user_id, language))
        sqlite_connection.commit()
        cursor.close()
        
    if sqlite_connection:
        sqlite_connection.close()

    return language


def update_user_language(user_id,language):
    # Connect (or create) DB sqlight3 for save user's language
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
    except sqlite3.Error as error:
        print('Error : ', error)
        
    # Update user language in DB
    cursor = sqlite_connection.cursor()
    cursor.execute("UPDATE user_language SET language = ? WHERE id = ?", (language, user_id))
    sqlite_connection.commit()
    cursor.close()
        
    if sqlite_connection:
        sqlite_connection.close()

    return language

    
# Commands
@bot.message_handler(commands=['start','en','fr','es','ru'])
def get_commands(command):
    
    # Get user language
    if command.text == '/start':
        language = get_user_language(str(command.from_user.id),str(command.from_user.language_code))         
    elif command.text == '/en':
        language = update_user_language(str(command.from_user.id),'en')
    elif command.text == '/fr':
        language = update_user_language(str(command.from_user.id),'fr')
    elif command.text == '/es':
        language = update_user_language(str(command.from_user.id),'es')
    elif command.text == '/ru':
        language = update_user_language(str(command.from_user.id),'ru')

    # Send first message
    if command.text in ['/start','/en','/fr','/es','/ru']:
    
        # Upload sticker
        sticker = open('img/question.png', 'rb')

        # First message from bot
        bot.send_sticker(command.from_user.id, sticker)
        bot.send_message(command.from_user.id, text=texts[language][1])

    else:
        # Unrecognized command
        bot.send_message(command.from_user.id, text=texts[language][3])


@bot.callback_query_handler(func=lambda call: True)
@bot.message_handler(content_types=['text'])
def answer(message):
    
    # Get user language
    language = get_user_language(str(message.from_user.id),str(message.from_user.language_code))  
        
    # Create button
    keyboard = telebot.types.InlineKeyboardMarkup()    
    button = telebot.types.InlineKeyboardButton(texts[language][2], callback_data='2')
    keyboard.add(button)

    # Ubload sticker
    photo_file = 'img/' + language + '/' + str(randint(1,20)) + '.png'
    sticker = open(photo_file, 'rb')
    bot.send_sticker(message.from_user.id, sticker, reply_markup=keyboard)


# Listen commmands from users
bot.infinity_polling(interval=0)