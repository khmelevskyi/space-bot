from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from src.variables import *
import src.config as c
from src.Logic.language_set import language
from src.Logic.menu import main_menu
from src.user_manager import UM, Partner


def partner_final_q(update, context):
    lang = language(update)
    answer = update.message.text
    if answer == c.text['final_option'][lang]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['final_answer'][lang])
        print(UM.currentUsers)
        return main_menu(update, context)
    elif answer == c.text['to_main_menu'][lang]:
        return main_menu(update, context)


def partner_email(update, context):
    lang = language(update)
    answer = update.message.text
    if len(answer) >= 3 and answer.count('@') == 1:
        UM.currentUsers[update.effective_chat.id].add_email(answer)
        reply_keyboard = [[c.text['final_option'][lang], c.text['to_main_menu'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['partner_q']['final_q'][lang].
                                  format(name=UM.currentUsers[update.effective_chat.id].get_name()),
                                  reply_markup=markup)
        return PARTNER_FINAL_Q
    else:
        update.message.reply_text(text=c.text['errors']['email'][lang], reply_markup=ReplyKeyboardRemove())
        return PARTNER_EMAIL


def partner_org_pos(update, context):
    lang = language(update)
    answer = update.message.text
    if len(answer) >= 2:
        UM.currentUsers[update.effective_chat.id].add_organization_position(answer)
        update.message.reply_text(text=c.text['partner_q']['email'][lang], reply_markup=ReplyKeyboardRemove())
        return PARTNER_EMAIL
    else:
        update.message.reply_text(text=c.text['errors']['organization_position'][lang], reply_markup=ReplyKeyboardRemove())
        return PARTNER_ORG_POS


def partner_org_name(update, context):
    lang = language(update)
    answer = update.message.text
    if len(answer) >= 2:
        UM.currentUsers[update.effective_chat.id].add_organization_name(answer)
        update.message.reply_text(text=c.text['partner_q']['organization_position'][lang], reply_markup=ReplyKeyboardRemove())
        return PARTNER_ORG_POS
    else:
        update.message.reply_text(text=c.text['errors']['organization_name'][lang], reply_markup=ReplyKeyboardRemove())
        return PARTNER_ORG_NAME


def partner_name(update, context):
    lang = language(update)
    answer = update.message.text
    try:
        a1, a2 = answer.split()
    except ValueError:
        update.message.reply_text(text=c.text['errors']['name'][lang], reply_markup=ReplyKeyboardRemove())
        return PARTNER_NAME
    if len(answer) >= 2 and a1.isalpha() and a2.isalpha():
        UM.create_user(Partner(update.effective_chat.id, answer.title(), 'partner'))
        update.message.reply_text(text=c.text['partner_q']['organization_name'][lang], reply_markup=ReplyKeyboardRemove())
        return PARTNER_ORG_NAME
    else:
        update.message.reply_text(text=c.text['errors']['name'][lang], reply_markup=ReplyKeyboardRemove())
        return PARTNER_NAME


def partner_handler(update, context):
    lang = language(update)
    answer = update.message.text
    if answer == c.text['partner_opt'][lang]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['partner_q']['answer'][lang])
        update.message.reply_text(text=c.text['partner_q']['name'][lang], reply_markup=ReplyKeyboardRemove())
        return PARTNER_NAME
    elif answer == c.text['to_main_menu'][lang]:
        return main_menu(update, context)


def partner(update, context):
    lang = language(update)
    reply_keyboard = [[c.text['partner_opt'][lang], c.text['to_main_menu'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text=c.text['partner'][lang], reply_markup=markup)
    return PARTNER_HANDLER
