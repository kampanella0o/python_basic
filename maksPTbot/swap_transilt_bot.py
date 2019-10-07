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
	bot.reply_to(message, "Hey, how are you doing? I'm here to help you switch between " 
                          "keyboard layouts or transliterate Cyrillics to Latin alphabet "
                          "(or vice versa)! Type '/convert' to start.")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "I can help you to switch between keyboard layouts or transliterate Cyrillics to "
                          "Latin alphabet (or vice versa). Send me '/convert' to start converting")

operation_buttons = ['Swap from Ru to En layout',
                     'Swap from En to Ru layout',
                     'Transliterate Cyrillics to Latin alphabet',
                     'Converts transliterated (Latin symbols) text back to Cyrillics']

@bot.message_handler(commands=['convert'])
def select_operation(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton(operation_buttons[0])
    itembtn2 = types.KeyboardButton(operation_buttons[1])
    itembtn3 = types.KeyboardButton(operation_buttons[2])
    itembtn4 = types.KeyboardButton(operation_buttons[3])
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    msg = bot.reply_to(message, "How can I help you?", reply_markup=markup)
    bot.register_next_step_handler(msg, input_text)

def input_text(message):
    operation_type = message.text
    markup = types.ReplyKeyboardRemove(selective=False)
    if operation_type not in operation_buttons:
        bot.reply_to(message, "Sorry, but you have to choose one of the predefined options.", reply_markup=markup)
        return select_operation(message)
    msg = bot.reply_to(message, "Ok, please enter the text to convert", reply_markup=markup)
    bot.register_next_step_handler(msg, convert_text, operation_type)

ru = 'ё1234567890-=йцукенгшщзхъфывапролджэ\\\\ячсмитьбю.Ё!"№;%:?*()_+ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ//ЯЧСМИТЬБЮ, '
en = '`1234567890-=qwertyuiop[]asdfghjkl;\'\\\\zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"||ZXCVBNM<>? '
swap_layout_dictionary = dict(zip(ru, en))

def ru_to_en_replacer(text, dictionary):
    for ru, en in dictionary.items():
        text = text.replace(ru, en)
    return text

def swap_ru_to_en(message):
    new_text = ru_to_en_replacer(message, swap_layout_dictionary)
    return new_text

def swap_en_to_ru(message):
    new_text = message
    for ru, en in swap_layout_dictionary.items():
        new_text = new_text.replace(en, ru)
    return new_text

translit_dictionary = {'ъ': '',
                        'щ': 'shch',
                        'ш': 'sh',
                        'ж': 'zh',
                        'х': 'kh',
                        'ц': 'ts',
                        'ч': 'ch',
                        'ю': 'iu',
                        'я': 'ia',
                        'а': 'a',
                        'б': 'b',
                        'в': 'v',
                        'г': 'g',
                        'д': 'd',
                        'е': 'e',
                        'ё': 'e',
                        'з': 'z',
                        'и': 'i',
                        'й': 'i',
                        'к': 'k',
                        'л': 'l',
                        'м': 'm',
                        'н': 'n',
                        'о': 'o',
                        'п': 'p',
                        'р': 'r',
                        'с': 's',
                        'т': 't',
                        'у': 'u',
                        'ф': 'f',
                        'ы': 'y',
                        'ь': '\'',
                        'э': 'e'}

def transilt_en_to_ru(message):
    new_string = message
    for ru, en in translit_dictionary.items():
        if en:
            new_string = new_string.replace(en, ru)
    return new_string

def transilt_ru_to_en(message):
    # new_string = message
    # for ru, en in translit_dictionary.items():
        # new_string = new_string.replace(ru, en)
    new_string = ru_to_en_replacer(message, translit_dictionary)
    return new_string

def convert_text(message, operation_type):
    try:
        markup = types.ReplyKeyboardRemove(selective=False)
        message_to_convert = message.text
        operations = {
            operation_buttons[0]: swap_ru_to_en,
            operation_buttons[1]: swap_en_to_ru,
            operation_buttons[2]: transilt_ru_to_en,
            operation_buttons[3]: transilt_en_to_ru
            }
        operation = operations.get(operation_type)
        bot.reply_to(message, "Here's your converted text:\n" + operation(message_to_convert), reply_markup=markup)
    except:
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, "Oops, something went wrong. Please check the data you enter and try again.", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Sorry, I don't understand you. Enter '/help' to see help.")

bot.polling()