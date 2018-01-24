import telegram
import serial
import time
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hola creador!')

def arduinoMssg(bot, update):
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    var = True
    while var:
        data_serial = int(arduino.readline().decode('UTF', 'ignore'))
        if data_serial > 30:
            print('Todo bien, distancia: %i' % data_serial)
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Alguien ha entrado, hora %s' % time.strftime('%H:%M:%S'))
            var = False
        time.sleep(1)

bot = telegram.Bot(token='528282587:AAHPIWWu7WB6dRE-rZfG7S673IODYn7WQ_g')
update = Updater(token='528282587:AAHPIWWu7WB6dRE-rZfG7S673IODYn7WQ_g')
dispatcher = update.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

start_handler = CommandHandler('start', start)
arduino_handler = CommandHandler('arduino', arduinoMssg)

dispatcher.add_handler(arduino_handler)
dispatcher.add_handler(start_handler)

update.start_polling()
