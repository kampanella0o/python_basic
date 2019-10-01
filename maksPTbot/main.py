# python_bot_env\Scripts\activate
import telebot
import os
from datetime import datetime
from schedule import SCHEDULE
from telebot.apihelper import ApiException
from config import token


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['time'])
def send_time(message):
	bot.reply_to(message, datetime.now())

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

# @bot.message_handler(content_types=['text'])
# def echo_all(message):
# 	# bot.reply_to(message, message.text)
# 	bot.send_message(message.chat.id, "Cool! Here's your message:")
# 	bot.send_message(message.chat.id, message.text)

try:
    os.mkdir("dialogs")
except FileExistsError:
    pass

@bot.message_handler(commands=['all'])
def send_three(message):
	try:
		with open('dialogs\\' + str(message.chat.id), encoding = 'utf-8', mode = 'r') as original_text:
			string = original_text.read()
			messages = string.split('\n----------\n')
			string_to_send = ("The last three messages are:\n" + messages[-4] + "\n" + messages[-3] + "\n" + messages[-2])
			bot.send_message(message.chat.id, string_to_send)
	except IndexError:
		bot.send_message(message.chat.id, "Send at least three text messages first!")
	except ApiException:
		bot.send_message(message.chat.id, "Send at least three text messages first!")

@bot.message_handler(commands=['delete'])
def delete_history(message):
	with open('dialogs\\' + str(message.chat.id), 'w'):
		pass

@bot.message_handler(content_types=['text'])
def send_schedule(message):
	with open('dialogs\\' + str(message.chat.id), encoding = 'utf-8', mode = 'a+') as original_text:
		original_text.write(message.text + '\n----------\n')

	if SCHEDULE.get(message.text):
		text = '\n'.join(SCHEDULE.get(message.text))
		bot.send_message(message.chat.id, text)

bot.polling()