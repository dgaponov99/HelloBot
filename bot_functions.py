import telebot
import os

import users_db
from res import string_values

bot = telebot.TeleBot(os.environ.get('TOKEN'))


def greeting(message):
    bot.send_message(message.chat.id, string_values.hello.format(message.from_user.first_name))


def adding(message):
    result = users_db.add_user(message.chat.id, message.from_user.first_name)
    if result:
        bot.send_message(os.environ.get('ADMIN'),
                         string_values.new_user.format(message.from_user.first_name, message.chat.id))


def reply_text(message):
    bot.send_message(message.chat.id, string_values.reply_hello)
