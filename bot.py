# -*- coding: utf-8 -*-

# Zdes bil vasyan

import requests
from telegram.ext import Updater
from telegram import ChatAction

def help(bot, update):
    message  = '/cat – рандомный котик\n'
    message += '/help – помощь\n'
    bot.sendMessage(update.message.chat_id, text=message)

def cat(bot, update):
    bot.sendChatAction(update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
    response = requests.get('http://random.cat/meow').json()
    bot.sendPhoto(update.message.chat_id, photo=str(response['file']))

def main():
    updater = Updater('138407653:AAEyd9-zuEqiODRC6JBfagfpZZdplV8gJZY')

    dp = updater.dispatcher
    dp.addTelegramCommandHandler("cat", cat)
    dp.addTelegramCommandHandler("help", help)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
