import telebot
import os

import users_db
from res import string_values

bot = telebot.TeleBot(os.environ.get('TOKEN'))


def send_hello():
    users = users_db.get_users()
    for user in users:
        bot.send_message(user['user_id'], string_values.send_goodmoning.format(user['first_name']))


send_hello()
