from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from variables import *
import config as c
from language_set import language
from main_menu import main_menu


def mentor_expertise(update, context): # not finished
    lang = language()
    answer = update.message.text
    if len(answer) >= 2:
        update.message.reply_text(text=c.text['mentor_q']['experience'][lang], reply_markup=ReplyKeyboardRemove())
        pass
    else:
        update.message.reply_text(text=c.text['errors']['expertise'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_EXPERTISE


def mentor_name(update, context): # not finished
    lang = language()
    answer = update.message.text
    try:
        a1, a2 = answer.split()
    except ValueError:
        update.message.reply_text(text=c.text['errors']['name'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_NAME
    if len(answer) >= 2 and a1.isalpha() and a2.isalpha():
        update.message.reply_text(text=c.text['mentor_q']['expertise'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_EXPERTISE
    else:
        update.message.reply_text(text=c.text['errors']['name'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_NAME


def mentor_handler(update, context):
    lang = language()
    answer = update.message.text
    if answer == c.text['mentor_opt'][lang]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['mentor_q']['answer'][lang])
        update.message.reply_text(text=c.text['mentor_q']['name'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_NAME
    elif answer == c.text['back'][lang]:
        return main_menu(update, context)


def mentor(update, context):
    lang = language()
    reply_keyboard = [[c.text['mentor_opt'][lang], c.text['back'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text=c.text['mentor'][lang], reply_markup=markup)
    return MENTOR_HANDLER
