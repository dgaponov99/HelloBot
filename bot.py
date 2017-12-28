import telebot
import os
from flask import Flask, request

import users_db
from res import string_values

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
    bot.send_message(message.chat.id, string_values.hello.format(message.from_user.first_name))
    result = users_db.add_user(message.chat.id, message.from_user.first_name)
    if result:
        bot.send_message(os.environ.get('ADMIN'),
                         string_values.new_user.format(message.from_user.first_name, message.chat.id))


@bot.message_handler(func=lambda message: True, content_types=['text'])
def text_message(message):
    bot.send_message(message.chat.id, string_values.reply_hello)


server.run(host="0.0.0.0", port=int(os.environ.get('PORT')))
