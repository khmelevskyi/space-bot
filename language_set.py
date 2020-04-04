from telegram import ReplyKeyboardMarkup
from src.variables import *
import src.config as c

from database import DbInterface
from os import getcwd

# get path of the database file and creating the manager object

path = getcwd() + "/Space_DB.db"
db = DbInterface(path)


def language(update):
    lang = db.getLang(update.message.chat_id)
    #print(update.effective_chat.id)
    if lang is None:
        update.message.reply_text(text=c.text['start'])
        reply_keyboard = [[c.text['ua'], c.text['en']]]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text(text=c.text['ask_lang'], reply_markup=markup)
        return lang
    else:
        return lang


def setting_lang(update, context):
    answer = update.message.text
    if answer == c.text["en"]:
        lang = 1
        db.setLang(update.effective_chat.id, lang)
    elif answer == c.text["ua"]:
        lang = 0
        db.setLang(update.effective_chat.id, lang)
    else:
        # if he inputs some shit we are not alowing to go further
        return language(update)

    markup = ReplyKeyboardMarkup([[c.text['to_main_menu'][lang]]], resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text=c.text['thanks'][lang], reply_markup=markup)
    return MAIN_MENU
