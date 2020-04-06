from telegram import ReplyKeyboardMarkup
from src.variables import *
from src.Logic.language_set import language
import src.config as c
from src.Logic.menu import main_menu

def about_yangel(update, context):
    lang = language(update)
    reply_keyboard = [[c.text['first_menu']['first_option'][lang], c.text['first_menu']['second_option'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    update.message.reply_text(text=c.text['one_answer'][lang], reply_markup=markup)
    return ABOUT_YANGEL_HANDLER

def about_yangel_handler(update, context):
    lang = language(update)
    answer = update.message.text
    if answer == c.text['first_menu']['first_option'][lang]:
        return main_menu(update, context)
    elif answer == c.text['first_menu']['second_option'][lang]:
        context.bot.send_message(text='http://www.nkau.gov.ua', chat_id=update.effective_chat.id)

