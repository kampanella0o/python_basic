# python_bot_env\Scripts\activate
import telebot
import os
import string 
import random
from telebot.apihelper import ApiException
from telebot import types
from config import token


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hey, how are you doing? I'm here to help you generate strong password! Type '/generate' to start.")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "I can generate several different types of passwords. Send me '/generate' to start generating one.")

@bot.message_handler(commands=['generate'])
def set_pass_type(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Only letters')
    itembtn2 = types.KeyboardButton('Only digits')
    itembtn3 = types.KeyboardButton('Letters and digits')
    itembtn4 = types.KeyboardButton('Letters, digits and symbols')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    msg = bot.send_message(message.chat.id, "Which type of password do you prefer?", reply_markup=markup)
    bot.register_next_step_handler(msg, set_pass_length)

def set_pass_length(message):
    pass_type = message.text
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('6')
    itembtn2 = types.KeyboardButton('8')
    itembtn3 = types.KeyboardButton('10')
    itembtn4 = types.KeyboardButton('12')
    itembtn5 = types.KeyboardButton('16')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    msg = bot.send_message(message.chat.id, "Ok, now please select the password length", reply_markup=markup)
    bot.register_next_step_handler(msg, generate_pass, pass_type)

letters = list(string.ascii_letters)
capital_letters = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(string.punctuation)

def password_filler(pass_length, list_of_characters):
    password = ''
    for i in range (0, pass_length):
        password += random.choice(list_of_characters)
    return password

def generate_letters_only_pass(pass_length):
    password = password_filler(pass_length, letters)
    validation = any(char in password for char in capital_letters)
    if not validation:
        return generate_letters_only_pass(pass_length)
    return password

def generate_digits_only_pass(pass_length):
    password = password_filler(pass_length, digits)
    return password

def generate_digits_letters_pass(pass_length):
    password = password_filler(pass_length, digits + letters)
    validation = any(char in password for char in capital_letters) and any(char in password for char in digits)
    if not validation:
        return generate_digits_letters_pass(pass_length)
    return password

def generate_everything_pass(pass_length):
    password = password_filler(pass_length, digits + letters + symbols)
    validation = any(char in password for char in capital_letters) and any(char in password for char in digits) and any(char in password for char in symbols)
    if not validation:
        return generate_everything_pass(pass_length)
    return password

def generate_pass(message, pass_type):
    try:
        markup = types.ReplyKeyboardRemove(selective=False)
        pass_length = int(message.text)
        generators = {
            'Only letters': generate_letters_only_pass,
            'Only digits': generate_digits_only_pass,
            'Letters and digits': generate_digits_letters_pass,
            'Letters, digits and symbols': generate_everything_pass
            }
        generator = generators.get(pass_type)
        bot.send_message(message.chat.id, "Here's your awesome password:\n" + generator(pass_length), reply_markup=markup)
    except:
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, "Oops, something went wrong. Please check the data you enter and try again.", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Sorry, I don't understand you. Enter '/help' to see help.")

bot.polling()