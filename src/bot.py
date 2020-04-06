from telegram.ext import Updater, Filters, ConversationHandler, MessageHandler, CommandHandler
from telegram import ReplyKeyboardMarkup #KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from os import environ as env, getcwd # for environmental variables
import logging #used for error detection

import src.config as c
from src.database import DbInterface
from src.Logic.language_set import language, setting_lang
from src.variables import *
from src.Logic.menu import main_menu
from src.Logic.about_yangel import about_yangel, about_yangel_handler
from src.Logic.mentor import mentor, mentor_handler, mentor_name, mentor_expertise, \
                        mentor_experience, mentor_site, mentor_email, mentor_final_q
from src.Logic.partner import partner, partner_handler, partner_name, partner_org_name, \
                        partner_org_pos, partner_email, partner_final_q
from src.Logic.startup import startup, tech_q, tech_yes_no, edu_yes_no, \
                        fantastic_yes_no, proto_yes_no, team_yes_no, \
                        q_round_yes_no, try_again_or_mm, startuper_name, \
                        startuper_email, startuper_idea, startuper_proto, \
                        startuper_why_we, startuper_final_q

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def main_menu_handler(update, context):
    lang = language(update)
    answer = update.message.text
    if answer == c.text['main_menu']['first_option'][lang]:
        return about_yangel(update, context)
    elif answer == c.text['main_menu']['second_option'][lang]:
        return startup(update, context)
    elif answer == c.text['main_menu']['third_option'][lang]:
        return mentor(update, context)
    elif answer == c.text['main_menu']['fourth_option'][lang]:
        return partner(update, context)


def start(update, context):
    """Welcome greating and proposing to choose the language"""
    lang = language(update)
    if lang == 1 or lang == 0:
        markup = ReplyKeyboardMarkup([[c.text['to_main_menu'][lang]]], resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['welcome_back'][lang], reply_markup=markup)
        return MAIN_MENU
    else:
        return LANG


def done(update, context):
    update.message.reply_text('END')
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    api_key = env.get('API_KEY')

    updater = Updater(token=api_key, use_context=True)
    dispatcher = updater.dispatcher

    necessary_handlers = [CommandHandler('start', start),
                          CommandHandler('stop', done)]

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            LANG: [MessageHandler(Filters.all, setting_lang), *necessary_handlers],
            MAIN_MENU: [MessageHandler(Filters.all, main_menu), *necessary_handlers],
            MAIN_MENU_HANDLER: [MessageHandler(Filters.all, main_menu_handler), *necessary_handlers],
            ABOUT_YANGEL: [MessageHandler(Filters.all, about_yangel), *necessary_handlers],
            ABOUT_YANGEL_HANDLER: [MessageHandler(Filters.all, about_yangel_handler), *necessary_handlers],
            STARTUP: [MessageHandler(Filters.all, startup), *necessary_handlers],
            TECH_OR_MM: [MessageHandler(Filters.all, tech_q), *necessary_handlers],
            TECH_YES_NO: [MessageHandler(Filters.all, tech_yes_no), *necessary_handlers],
            PROTOTYPE_YES_NO: [MessageHandler(Filters.text, proto_yes_no), *necessary_handlers],
            EDU_YES_NO: [MessageHandler(Filters.text, edu_yes_no), *necessary_handlers],
            TEAM_YES_NO: [MessageHandler(Filters.text, team_yes_no), *necessary_handlers],
            TRY_AGAIN_OR_MM: [MessageHandler(Filters.text, try_again_or_mm), *necessary_handlers],
            FANTASTIC_YES_NO: [MessageHandler(Filters.text, fantastic_yes_no), *necessary_handlers],
            Q_ROUND_YES_NO: [MessageHandler(Filters.text, q_round_yes_no), *necessary_handlers],
            STARTUPER_NAME: [MessageHandler(Filters.text, startuper_name), *necessary_handlers],
            STARTUPER_EMAIL: [MessageHandler(Filters.text, startuper_email), *necessary_handlers],
            STARTUPER_IDEA: [MessageHandler(Filters.text, startuper_idea),*necessary_handlers],
            STARTUPER_PROTO: [MessageHandler(Filters.text, startuper_proto), *necessary_handlers],
            STARTUPER_WHY: [MessageHandler(Filters.text, startuper_why_we), *necessary_handlers],
            STARTUPER_FINAL_Q: [MessageHandler(Filters.text, startuper_final_q), *necessary_handlers],
            MENTOR_HANDLER: [MessageHandler(Filters.text, mentor_handler), *necessary_handlers],
            MENTOR_NAME: [MessageHandler(Filters.text, mentor_name), *necessary_handlers],
            MENTOR_EXPERTISE: [MessageHandler(Filters.text, mentor_expertise), *necessary_handlers],
            MENTOR_EXPERIENCE: [MessageHandler(Filters.text, mentor_experience), *necessary_handlers],
            MENTOR_SITE: [MessageHandler(Filters.all, mentor_site), *necessary_handlers],
            MENTOR_EMAIL: [MessageHandler(Filters.all, mentor_email), *necessary_handlers],
            MENTOR_FINAL_Q: [MessageHandler(Filters.text, mentor_final_q), *necessary_handlers],
            PARTNER: [MessageHandler(Filters.text, partner), *necessary_handlers],
            PARTNER_HANDLER: [MessageHandler(Filters.text, partner_handler), *necessary_handlers],
            PARTNER_NAME: [MessageHandler(Filters.text, partner_name), *necessary_handlers],
            PARTNER_ORG_NAME: [MessageHandler(Filters.text, partner_org_name), *necessary_handlers],
            PARTNER_ORG_POS: [MessageHandler(Filters.text, partner_org_pos), *necessary_handlers],
            PARTNER_EMAIL: [MessageHandler(Filters.all, partner_email), *necessary_handlers],
            PARTNER_FINAL_Q: [MessageHandler(Filters.text, partner_final_q), *necessary_handlers]

        },
        conversation_timeout=1800,

        fallbacks=[CommandHandler('stop', done)],
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
