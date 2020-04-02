from telegram import ReplyKeyboardMarkup
from variables import *
from language_set import language
import config as c
from menu import main_menu


def about_yangel_handler(update, context):
    lang = language()
    answer = update.message.text
    if answer == c.text['first_menu']['first_option'][lang]:
        return main_menu(update, context)
    elif answer == c.text['first_menu']['second_option'][lang]:
        context.bot.send_message(text='http://www.nkau.gov.ua', chat_id=update.effective_chat.id)


def about_yangel(update, context):
    lang = language()
    reply_keyboard = [[c.text['first_menu']['first_option'][lang], c.text['first_menu']['second_option'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    update.message.reply_text(text=c.text['one_answer'][lang], reply_markup=markup)
    return ABOUT_YANGEL_HANDLER

