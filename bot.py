import telebot
import os
from flask import Flask, request

import bot_functions

bot = telebot.TeleBot(os.environ.get('TOKEN'))

server = Flask(__name__)


@server.route("/" + os.environ.get('TOKEN'), methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=os.environ.get('URL') + os.environ.get('TOKEN'))
    return "!", 200


@bot.message_handler(commands=['start'])
def command_start(message):
    bot_functions.greeting(message)
    bot_functions.add_user(message)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def text_message(message):
    bot_functions.reply_text(message)


server.run(host="0.0.0.0", port=int(os.environ.get('PORT')))
