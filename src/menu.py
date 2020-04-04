from telegram import ReplyKeyboardMarkup
import src.config as c
from src.variables import *
from language_set import language


def main_menu(update, context):
    lang = language(update)
    answer = update.message.text
    if (answer == c.text['back'][lang] or
            answer == c.text['to_main_menu'][lang] or
            answer == c.text['first_menu']['first_option'][lang] or
            answer == c.text['en'] or answer == c.text['ua']):
        reply_keyboard = [[c.text['main_menu']['first_option'][lang], c.text['main_menu']['second_option'][lang]],
                          [c.text['main_menu']['third_option'][lang], c.text['main_menu']['fourth_option'][lang]],
                          [c.text['main_menu']['fifth_option'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
        update.message.reply_text(text=c.text['help_ask'][lang], reply_markup=markup)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Unknown command')
    return MAIN_MENU_HANDLER
