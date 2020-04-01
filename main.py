from telegram.ext import Updater, Filters, ConversationHandler, MessageHandler
from telegram.ext import CommandHandler # handles with user's commands
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ as env # for environmental variables
import logging #used for error detection
import TgBot.config as c

LANG, MAIN_MENU, MAIN_MENU_HANDLER, ABOUT_YANGEL, ABOUT_YANGEL_HANDLER, STARTUP, STARTUP_HANDLER_FIRST = range(7)
lang = 0

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def startup_handler_first(update, context):
    answer = update.message.text
    if answer == c.text['lets_go'][lang]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['startup_ans']['first'][lang])
        reply_keyboard = [[c.text['yes'][lang], c.text['no'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_q']['tech'][lang], reply_markup=markup)
    elif answer == c.text['back'][lang]:
        return main_menu(update, context)


def startup(update, context):
    reply_keyboard = [[c.text['lets_go'][lang], c.text['back'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text=c.text['startup'][lang], reply_markup=markup)
    return STARTUP_HANDLER_FIRST


def about_yangel_handler(update, context):
    answer = update.message.text
    if answer == c.text['first_menu']['first_option'][lang]:
        return main_menu(update, context)
    elif answer == c.text['first_menu']['second_option'][lang]:
        context.bot.send_message(text='http://www.nkau.gov.ua', chat_id=update.effective_chat.id)


def about_yangel(update, context):
    reply_keyboard = [[c.text['first_menu']['first_option'][lang], c.text['first_menu']['second_option'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    update.message.reply_text(text=c.text['one_answer'][lang], reply_markup=markup)
    return ABOUT_YANGEL_HANDLER


def main_menu_handler(update, context):
    global lang
    answer = update.message.text
    if answer == c.text['main_menu']['first_option'][lang]:
        return about_yangel(update, context)
    elif answer == c.text['main_menu']['second_option'][lang]:
        return startup(update, context)


def main_menu(update, context):
    global lang
    reply_keyboard = [[c.text['main_menu']['first_option'][lang], c.text['main_menu']['second_option'][lang]],
                      [c.text['main_menu']['third_option'][lang], c.text['main_menu']['fourth_option'][lang]],
                      [c.text['main_menu']['fifth_option'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    update.message.reply_text(text=c.text['help_ask'][lang], reply_markup=markup)
    return MAIN_MENU_HANDLER


def setting_lang(update, context):
    global lang
    if update.message.text == c.text["en"]:
        lang = 1
    return main_menu(update, context)


def start(update, context):
    global lang
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hi! I’m Maryna, Yangel Accelerator onboarding bot.')
    reply_keyboard = [[c.text['ua'], c.text['en']]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(text=c.text['ask_lang'][lang], reply_markup=markup)
    return LANG


def done(update, context):
    update.message.reply_text('END')
    return ConversationHandler.END


def main():
    api_key = env.get('API_KEY')

    updater = Updater(token=api_key, use_context=True)
    dispatcher = updater.dispatcher

    necessary_hendlers = [CommandHandler('start', start),
                          CommandHandler('stop', done)]

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            LANG: [MessageHandler(Filters.all, setting_lang), *necessary_hendlers],
            MAIN_MENU: [MessageHandler(Filters.all, main_menu), *necessary_hendlers],
            MAIN_MENU_HANDLER: [MessageHandler(Filters.all, main_menu_handler), *necessary_hendlers],
            ABOUT_YANGEL: [MessageHandler(Filters.all, about_yangel), *necessary_hendlers],
            ABOUT_YANGEL_HANDLER: [MessageHandler(Filters.all, about_yangel_handler), *necessary_hendlers],
            STARTUP: [MessageHandler(Filters.all, startup), *necessary_hendlers],
            STARTUP_HANDLER_FIRST: [MessageHandler(Filters.all, startup_handler_first), *necessary_hendlers],

        },

        fallbacks=[CommandHandler('stop', done)]
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()






