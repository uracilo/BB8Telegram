import telegram
import os
import logging
import serial
import time
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

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

def arduinoMensaje(bot, update):
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    var = True
    while var:
        data_serial = int(arduino.readline().decode('UTF', 'ignore'))
        if data_serial < 30:
            bot.send_message(chat_id=update.message.chat_id, text='Alguien entró, hora: %s' % time.strftime('%H:%M:%S'))
            print('Alguien ha entrado, distancia: %i' % data_serial)
            var = False
        else:
            print('Todo bien, distancia: %i' % data_serial)
        time.sleep(1)

bot = telegram.Bot(token='511608051:AAGCNTd7WBiK5gfSA69hwyvG75S76H-_HUw')
update = Updater(token='511608051:AAGCNTd7WBiK5gfSA69hwyvG75S76H-_HUw')
dispatcher = update.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
arduino_handler = CommandHandler('arduino', arduinoMensaje)
dispatcher.add_handler(arduino_handler)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)
sendFile_handler = CommandHandler('sendFile', sendFile, pass_args=True)
dispatcher.add_handler(sendFile_handler)
update.start_polling()
