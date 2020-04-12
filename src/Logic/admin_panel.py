from telegram import ReplyKeyboardMarkup
import csv
from datetime import datetime
from os import getcwd

from Logic.menu import main_menu, unknown_command
from Logic.language_set import language
import config as c
from variables import *
from database import db
#from Logic.stats_manager import Statistics
import Logic.graph_create
import subprocess


def stats_handler(update, context, specialization):
    date_data = db.get_date(specialization)
    with open('datetime.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'count'])
        i = 1
        for z in date_data:
            writer.writerow([datetime.fromtimestamp(z).date(), i])
        file.close()
    path = getcwd() + "/src/Logic/graph_create.py"
    subprocess.run(f'python3 {path}', shell=True)
    filename = getcwd() + '/graph.png'
    with open(filename, 'rb') as file:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=file,
                               caption='The graph')


def get_stats(update, context):
    lang = language(update)
    answer = update.message.text
    # context.bot.send_message(chat_id=update.effective_chat.id, text=statistics.get_stats(lang))
    # get_date
    if answer == c.text['options_admin']['startup'][lang]:
        return stats_handler(update, context, 'startup')
    elif answer == c.text['options_admin']['mentor'][lang]:
        return stats_handler(update, context, 'mentor')
    elif answer == c.text['options_admin']['partner'][lang]:
        return stats_handler(update, context, 'partner')
    elif answer == c.text['back'][lang]:
        return admin(update, context)
    else:
        return unknown_command(update, context)


def push_who(update, context):
    lang = language(update)
    answer = update.message.text
    # get_users
    pass


def admin_handler(update, context):
    lang = language(update)
    answer = update.message.text
    if answer == c.text['options_admin']['push'][lang]:
        reply_keyboard = [[c.text['options_admin']['all'][lang], c.text['options_admin']['startup'][lang]],
                          [c.text['options_admin']['mentor'][lang], c.text['options_admin']['partner'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['push_q'][lang], reply_markup=markup)
        pass #return PUSH_WHO, then PUSH_TEXT, PUSH_FINAL
    elif answer == c.text['options_admin']['stats'][lang]:
        reply_keyboard = [[c.text['options_admin']['startup'][lang], c.text['options_admin']['mentor'][lang]],
                          [c.text['options_admin']['partner'][lang], c.text['back']]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['stats_q'][lang], reply_markup=markup)
        return GET_STATS
    elif answer == c.text['to_main_menu'][lang]:
        return main_menu(update, context)
    else:
        return unknown_command(update, context)


def admin(update, context):
    lang = language(update)
    if update.message.chat.username in ('khmellevskyi', 'V_Vargan'):
        reply_keyboard = [[c.text['options_admin']['push'][lang], c.text['options_admin']['stats'][lang]],
                          [c.text['to_main_menu'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['hi_boss'][lang], reply_markup=markup)
        return ADMIN_HANDLER
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['sorry_not_boss'][lang])
