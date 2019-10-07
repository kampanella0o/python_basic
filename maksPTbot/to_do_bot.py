# python_bot_env\Scripts\activate
import telebot
import re
import os
import string 
import random
from telebot.apihelper import ApiException
from telebot import types
from config import token
from event_for_todo_bot import Event
from datetime import datetime, date, time



bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hey, how are you doing? I'm here to help you keep all your tasks. "
    "Send me /add_task to add your first task or /help to see other commands")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "You can use the next commands:\n"
    "/add_task to add new task\n"
    "/todo to see the list of unfinished tasks\n"
    "/all to see the list of all the tasks\n"
    "/complete %task_number% to mark task as complete\n"
    "/delete %task_number% to delete task\n"
    "/clear to delete ALL the tasks in the list")

tasks_list = []

@bot.message_handler(commands=['add_task'])
def enter_task_name(message):
    msg = bot.send_message(message.chat.id, "Enter the name of the task")
    bot.register_next_step_handler(msg, enter_task_date)

def enter_task_date(message):
    task_name = message.text
    msg = bot.send_message(message.chat.id, "Enter the task date (ONLY in format DD.MM.YYYY e.g. 05.11.2019)")
    bot.register_next_step_handler(msg, enter_task_time, task_name)

def enter_task_time(message, task_name):
    task_date = message.text
    if re.match(r'\d\d.\d\d.\d{4}', task_date):
        numbers = task_date.split('.')
        if int(numbers[0]) in range(1, 32) and\
            int(numbers[1]) in range(1, 13) and\
            int(numbers[2]) >= 2019:
                pass
        else:
            bot.reply_to(message, "Please enter a valid date (ONLY in format DD.MM.YYYY e.g. 05.11.2019)")
            return enter_task_date(message)
    else:
        bot.reply_to(message, "Please enter a valid date (ONLY in format DD.MM.YYYY e.g. 05.11.2019)")
        return enter_task_date(message)

    msg = bot.send_message(message.chat.id, "Enter the task time (ONLY in format HH.MM, e.g. 06.30)")
    bot.register_next_step_handler(msg, add_task, task_name, task_date)

def add_task(message, task_name, task_date):
    task_time = message.text

    if not re.match(r'\d\d.\d\d', task_time):
        bot.reply_to(message, "Please enter a valid time (ONLY in format HH.MM, e.g. 06.30)")
        return enter_task_time(message, task_name)

    numbers = task_time.split('.')
    if int(numbers[0]) not in range(0, 24) or int(numbers[1]) not in range(0, 60):
        bot.reply_to(message, "Please enter a valid time (ONLY in format HH.MM, e.g. 06.30)")
        return enter_task_time(message, task_name)

    task_datetime = datetime.combine(datetime.strptime(task_date, '%d.%m.%Y').date(), datetime.strptime(task_time,'%H.%M').time())
    
    if task_datetime < datetime.now():
        bot.reply_to(message, "Task date and time should be in future. Please, try again")
        return enter_task_date(message)
    
    tasks_list.append(Event(task_name, task_date, task_time))
    bot.send_message(message.chat.id, "Ok, I've added the task " + str(tasks_list[-1]))


@bot.message_handler(commands=['all'])
def show_all(message):
    tasks_list.sort(key= lambda x: x.date_time)
    list_to_show = []
    i = 1
    for task in tasks_list:
        list_to_show.append(str(i) + '. ' + str(task))
        i += 1
    if list_to_show:
        bot.send_message(message.chat.id, "Here're all your tasks:\n" + '\n'.join(list_to_show))
    else:
        bot.send_message(message.chat.id, "Seems that you have no any tasks.")

@bot.message_handler(commands=['todo'])
def show_active(message):
    tasks_list.sort(key= lambda x: x.date_time)
    list_to_show = []
    i = 1
    for task in tasks_list:
        if task.status == " - TO DO":
            list_to_show.append(str(i) + '. ' + str(task))
            i += 1
    if list_to_show:
        bot.send_message(message.chat.id, "Here're your unfinished tasks:\n" + '\n'.join(list_to_show))
    else:
        bot.send_message(message.chat.id, "Seems that you have no unfinished tasks.")

@bot.message_handler(commands=['complete'])
def complete_task_by_number(message):
    task_number = message.text.split()[1]
    tasks_list[int(task_number)-1].status = ' - DONE'
    bot.send_message(message.chat.id, "OK, I've marked %s as completed" % tasks_list[int(task_number)-1].task_name)

@bot.message_handler(commands=['delete'])
def delete_task_by_number(message):
    task_number = message.text.split()[1]
    deleted_task_name = tasks_list[int(task_number)-1].task_name
    del tasks_list[int(task_number)-1]
    bot.send_message(message.chat.id, "OK, I've deleted %s" % deleted_task_name)

@bot.message_handler(commands=['clear'])
def clear_list_of_tasks(message):
    tasks_list.clear()
    bot.send_message(message.chat.id, "OK, I've cleared the list of tasks")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Sorry, I don't understand you. Enter '/help' to see help.")

bot.polling()