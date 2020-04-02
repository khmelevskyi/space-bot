from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from variables import *
import config as c
from language_set import language
from main_menu import main_menu


def try_again_or_mm(update, context): # try again(go to question about tech) or move to main menu
    lang = language()
    answer = update.message.text
    if answer == c.text['try_again'][lang]:
        return tech_yes_no(update, context)
    elif answer == c.text['to_main_menu'][lang]:
        return main_menu(update, context)


### team, prototype and qualification round
def q_round_yes_no(update, context):
    lang = language()
    answer = update.message.text
    if answer == c.text['yes'][lang]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['startup_ans']['fifth'][lang])
        update.message.reply_text(text=c.text['startup_blank_q']['name'][lang], reply_markup=ReplyKeyboardRemove())
        pass ##################################### fill the blank
    elif answer == c.text['to_main_menu'][lang]:
        return main_menu(update, context)


def team_yes_no(update, context):
    lang = language()
    answer = update.message.text
    if answer == c.text['yes'][lang]:
        reply_keyboard = [[c.text['yes'][lang], c.text['to_main_menu'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_q']['q_round'][lang], reply_markup=markup)
        return Q_ROUND_YES_NO
    elif answer == c.text['no'][lang]:
        reply_keyboard = [[c.text['to_main_menu'][lang], c.text['try_again'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_ans']['third'][lang], reply_markup=markup)
        return TRY_AGAIN_OR_MM # try again(go to question about tech) or move to main menu


def proto_yes_no(update, context):
    lang = language()
    answer = update.message.text
    if answer == c.text['yes'][lang]:
        reply_keyboard = [[c.text['yes'][lang], c.text['no'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_q']['team'][lang], reply_markup=markup)
        return TEAM_YES_NO
    elif answer == c.text['no'][lang]:
        reply_keyboard = [[c.text['to_main_menu'][lang], c.text['try_again'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_ans']['second'][lang], reply_markup=markup)
        return TRY_AGAIN_OR_MM
### team, prototype and qualification round


### tech, edu and fantastic questions
def fantastic_yes_no(update, context): # if the answer to fantastic question is no, it means that the project is not
    lang = language() # related to the space at all
    answer = update.message.text
    if answer == c.text['yes'][lang]:
        reply_keyboard = [[c.text['yes'][lang], c.text['no'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_q']['prototype'][lang], reply_markup=markup)
        return PROTOTYPE_YES_NO
    elif answer == c.text['no'][lang]:
        reply_keyboard = [[c.text['to_main_menu'][lang], c.text['try_again'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_ans']['fourth'][lang], reply_markup=markup)
        return TRY_AGAIN_OR_MM


def edu_yes_no(update, context):
    lang = language()
    answer = update.message.text
    if answer == c.text['yes'][lang]:
        reply_keyboard = [[c.text['yes'][lang], c.text['no'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_q']['prototype'][lang], reply_markup=markup)
        return PROTOTYPE_YES_NO
    elif answer == c.text['no'][lang]:
        reply_keyboard = [[c.text['yes'][lang], c.text['no'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_q']['fantastic'][lang], reply_markup=markup)
        return FANTASTIC_YES_NO


def tech_yes_no(update, context): # takes the answer from tech_q(about tech question) and (if answer for tech_q is yes)
    lang = language()  # returns the answer for prototype question(yes or no) or (if answer for tech_q is no)
    answer = update.message.text  # returns the answer for education question
    if answer == c.text['yes'][lang] or answer == c.text['try_again'][lang]:
        reply_keyboard = [[c.text['yes'][lang], c.text['no'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_q']['prototype'][lang], reply_markup=markup)
        return PROTOTYPE_YES_NO
    elif answer == c.text['no'][lang]:
        reply_keyboard = [[c.text['yes'][lang], c.text['no'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_q']['edu'][lang], reply_markup=markup)
        return EDU_YES_NO


def tech_q(update, context): #takes the answer from the prev question, if answer is 'let's go' - makes two buttons: yes
    lang = language() # or no, and sends the next question, then returns the answer of this question
    answer = update.message.text
    if answer == c.text['lets_go'][lang]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['startup_ans']['first'][lang])
        reply_keyboard = [[c.text['yes'][lang], c.text['no'][lang]]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(text=c.text['startup_q']['tech'][lang], reply_markup=markup)
        return TECH_YES_NO
    elif answer == c.text['back'][lang]:
        return main_menu(update, context)
### tech, edu and fantastic questions


def startup(update, context):
    lang = language()
    reply_keyboard = [[c.text['lets_go'][lang], c.text['back'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text=c.text['startup'][lang], reply_markup=markup)
    return TECH_OR_MM
