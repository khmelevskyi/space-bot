from telegram import ReplyKeyboardMarkup
from variables import *
import config as c
lang = 0


def language():
    global lang
    lang = lang
    return lang


def setting_lang(update, context):
    global lang
    answer = update.message.text
    if answer == c.text['en']:
        lang = 1
    markup = ReplyKeyboardMarkup([[c.text['to_main_menu'][lang]]], resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text=c.text['thanks'][lang], reply_markup=markup)
    return MAIN_MENU
