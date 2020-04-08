from telegram import ReplyKeyboardMarkup, PhotoSize
from os import getcwd
import config as c
from variables import *
from Logic.language_set import language


def main_menu(update, context):
    lang = language(update)
    answer = update.message.text
    if (answer == c.text['back'][lang] or
            answer == c.text['to_main_menu'][lang] or
            answer == c.text['first_menu']['first_option'][lang] or
            answer == c.text['en'] or answer == c.text['ua'] or
            answer == c.text['final_option'][lang] or answer == c.text['no'][lang]):
        reply_keyboard = [[c.text['main_menu']['first_option'][lang], c.text['main_menu']['second_option'][lang]],
                          [c.text['main_menu']['third_option'][lang], c.text['main_menu']['fourth_option'][lang]],
                          [c.text['main_menu']['fifth_option'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
        update.message.reply_text(text=c.text['help_ask'][lang], reply_markup=markup)
        return MAIN_MENU_HANDLER
    else:
        return unknown_command(update, context)


def unknown_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Unknown command')
    filename = getcwd() + '/src/Logic/photo.png'
    #picture = PhotoSize(getcwd() + '/src/Logic/', 'photo.png', width=120, height=50)
    with open(filename, 'rb') as file:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=file, caption='Press this button and choose the option')
