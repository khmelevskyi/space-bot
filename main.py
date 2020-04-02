from telegram.ext import Updater, Filters, ConversationHandler, MessageHandler
from telegram.ext import CommandHandler # handles with user's commands
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove #KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from os import environ as env # for environmental variables
import logging #used for error detection
import config as c

LANG, MAIN_MENU, MAIN_MENU_HANDLER, ABOUT_YANGEL, ABOUT_YANGEL_HANDLER, STARTUP, TECH_OR_MM, \
TECH_YES_NO, PROTOTYPE_YES_NO, EDU_YES_NO, TEAM_YES_NO, FANTASTIC_YES_NO, TRY_AGAIN_OR_MM, Q_ROUND_YES_NO, \
MENTOR_HANDLER, MENTOR_NAME, MENTOR_EXPERTISE = range(17)

lang = 0
name = ''


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
'''MENTOR'''


def mentor_expertise(update, context): # not finished, not correct
    answer = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['mentor_q']['final_q'][lang].format(name=name))


def mentor_name(update, context):
    global name
    answer = update.message.text
    try:
        a1, a2 = answer.split()
    except ValueError:
        update.message.reply_text(text='Enter both: name and lastname', reply_markup=ReplyKeyboardRemove())
        return MENTOR_NAME
    if len(answer) >= 2 and a1.isalpha() or a2.isalpha():
        name = a1
        with open('some_file', 'w') as file:
            file.write(answer.title())
            file.close()
        update.message.reply_text(text=c.text['mentor_q']['expertise'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_EXPERTISE
    else:
        update.message.reply_text(text='Enter your name and lastname properly', reply_markup=ReplyKeyboardRemove())
        return MENTOR_NAME


def mentor_handler(update, context):
    answer = update.message.text
    if answer == c.text['mentor_opt'][lang]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['mentor_q']['answer'][lang])
        update.message.reply_text(text=c.text['mentor_q']['name'][lang], reply_markup=ReplyKeyboardRemove())
        return MENTOR_NAME
    elif answer == c.text['back'][lang]:
        return main_menu(update, context)


def mentor(update, context):
    reply_keyboard = [[c.text['mentor_opt'][lang], c.text['back'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text=c.text['mentor'][lang], reply_markup=markup)
    return MENTOR_HANDLER


'''MENTOR'''
'''STARTUP'''


def try_again_or_mm(update, context): # try again(go to question about tech) or move to main menu
    answer = update.message.text
    if answer == c.text['try_again'][lang]:
        return tech_yes_no(update, context)
    elif answer == c.text['to_main_menu'][lang]:
        return main_menu(update, context)


### team, prototype and qualification round
def q_round_yes_no(update, context):
    answer = update.message.text
    if answer == c.text['yes'][lang]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=c.text['startup_ans']['fifth'][lang])
        update.message.reply_text(text=c.text['startup_blank_q'][lang], reply_markup=ReplyKeyboardRemove())
        pass ##################################### fill the blank
    elif answer == c.text['to_main_menu'][lang]:
        return main_menu(update, context)


def team_yes_no(update, context):
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
    answer = update.message.text # related to the space at all
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
    answer = update.message.text  # returns the answer for prototype question(yes or no) or (if answer for tech_q is no)
    if answer == c.text['yes'][lang] or answer == c.text['try_again'][lang]: # returns the answer for education question
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
    answer = update.message.text # or no, and sends the next question, then returns the answer of this question
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
    reply_keyboard = [[c.text['lets_go'][lang], c.text['back'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text=c.text['startup'][lang], reply_markup=markup)
    return TECH_OR_MM


'''STARTUP'''
'''ABOUT YANGEL'''


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


'''ABOUT YANGEL'''


### main menu
def main_menu_handler(update, context):
    global lang
    answer = update.message.text
    if answer == c.text['main_menu']['first_option'][lang]:
        return about_yangel(update, context)
    elif answer == c.text['main_menu']['second_option'][lang]:
        return startup(update, context)
    elif answer == c.text['main_menu']['third_option'][lang]:
        return mentor(update, context)


def main_menu(update, context):
    global lang
    reply_keyboard = [[c.text['main_menu']['first_option'][lang], c.text['main_menu']['second_option'][lang]],
                      [c.text['main_menu']['third_option'][lang], c.text['main_menu']['fourth_option'][lang]],
                      [c.text['main_menu']['fifth_option'][lang]]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    update.message.reply_text(text=c.text['help_ask'][lang], reply_markup=markup)
    return MAIN_MENU_HANDLER
### main menu


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


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


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
            TECH_OR_MM: [MessageHandler(Filters.all, tech_q), *necessary_hendlers],
            TECH_YES_NO: [MessageHandler(Filters.all, tech_yes_no), *necessary_hendlers],
            PROTOTYPE_YES_NO: [MessageHandler(Filters.text, proto_yes_no), *necessary_hendlers],
            EDU_YES_NO: [MessageHandler(Filters.text, edu_yes_no), *necessary_hendlers],
            TEAM_YES_NO: [MessageHandler(Filters.text, team_yes_no), *necessary_hendlers],
            TRY_AGAIN_OR_MM: [MessageHandler(Filters.text, try_again_or_mm), *necessary_hendlers],
            FANTASTIC_YES_NO: [MessageHandler(Filters.text, fantastic_yes_no), *necessary_hendlers],
            Q_ROUND_YES_NO: [MessageHandler(Filters.text, q_round_yes_no), *necessary_hendlers],
            MENTOR_HANDLER: [MessageHandler(Filters.text, mentor_handler), *necessary_hendlers],
            MENTOR_NAME: [MessageHandler(Filters.text, mentor_name), *necessary_hendlers],
            MENTOR_EXPERTISE: [MessageHandler(Filters.text, mentor_expertise), *necessary_hendlers],

        },

        fallbacks=[CommandHandler('stop', done)]
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()






