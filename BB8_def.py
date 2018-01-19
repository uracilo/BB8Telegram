import telegram
import os
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters as f

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hola!')

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    text_caps = ''.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

def sendFile(bot, update, args):
    path = '/home/aldorvv/' + args[0]
    try:
        if(not os.path.isfile(path)):
            bot.send_message(chat_id=update.message.chat_id, text='Lo siento, eso no es un archivo')
            bot.send_message(chat_id=update.message.chat_id, text='Ruta del archivo: %s' % path)
        else:
            f = open(path, 'rb')
            bot.send_document(chat_id=update.message.chat_id,document=f)
    except:
        bot.send_message(chat_id=update.message.chat_id, text='No lo encontré :c')
        bot.send_message(chat_id=update.message.chat_id, text='Archivo: %s' % path)
