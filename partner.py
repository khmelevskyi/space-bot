from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from variables import *
import config as c
from language_set import language
from main_menu import main_menu


def partner_handler(update, context):
    lang = language()
    answer = update.message.text
    if answer == c.text['partner_opt'][lang]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['partner_q']['answer'][lang])
        update.message.reply_text(text=c.text['partner_q']['name'][lang], reply_markup=ReplyKeyboardRemove())
        pass #return PARTNER_NAME
    elif answer == c.text['to_main_menu'][lang]:
        return main_menu(update, context)


def partner(update, context):
    lang = language()
    reply_keyboard = [[c.text['partner_opt'][lang], c.text['to_main_menu'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text=c.text['partner'][lang], reply_markup=markup)
    return PARTNER_HANDLER
