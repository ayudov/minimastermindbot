from telebot.types import Message
from random import randint, random, getrandbits, shuffle, sample

from bot import bot
import texts.text as text
import states
import buttons
import config_google_spreadsheet as cgs


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    if str(message.from_user.id) in cgs.sheet.sheet1.col_values(2):
        bot.send_message(message.chat.id, "С возвращением, " + str(message.from_user.first_name) + "!")
    else:
        row = [cgs.get_number_of_rows(cgs.sheet),
               message.from_user.id,
               message.from_user.first_name,
               message.from_user.last_name,
               "@" + message.from_user.username,
               states.CHOOSE_LANGUAGE,
               "NONE",
               "NONE",
               "NONE",
               "NONE",
               "NONE"]
        cgs.sheet.sheet1.insert_row(row, cgs.get_number_of_rows(cgs.sheet) + 1)
        bot.send_message(message.chat.id, text.HELLO_MESSAGE, parse_mode='HTML')#, reply_markup=buttons.keyboard_choose_lang)+ text.HELLO_MESSAGE_RUS + "</b>\n" +
                         # text.CHOOSE_LANGUAGE,+ text.CHOOSE_LANGUAGE_RUS,


@bot.message_handler(commands=['change_language_to_eng'])
def set_ENG_language(message: Message):
    if cgs.get_user_language(message.from_user.id) == "English":
        bot.send_message(message.chat.id, "This language is already set")
    else:
        cgs.sheet.sheet1.update_cell(cgs.get_user_row(user_id=message.from_user.id), cgs.LANGUAGE_COL, "English")
        message_text = getattr(text, cgs.get_user_language(message.from_user.id) + "_set")()
        bot.send_message(message.chat.id, message_text)



@bot.message_handler(commands=['change_language_to_rus'])
def set_ENG_language(message: Message):
    if cgs.get_user_language(message.from_user.id) == "Russian":
        bot.send_message(message.chat.id, "Этот язык уже установлен")
    else:
        cgs.sheet.sheet1.update_cell(cgs.get_user_row(user_id=message.from_user.id), cgs.LANGUAGE_COL, "Russian")
        message_text = getattr(text, cgs.get_user_language(message.from_user.id) + "_set")()
        bot.send_message(message.chat.id, message_text)


@bot.message_handler(commands=['help'])
def help(message: Message):
    if cgs.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    else:
        message_text = getattr(text, cgs.get_user_language(message.from_user.id) + "_help_text")()
        bot.send_message(message.chat.id, message_text,  parse_mode='HTML')


@bot.message_handler(commands=['about_author'])
def about_author(message: Message):
    if cgs.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    else:
        message_text = getattr(text, cgs.get_user_language(message.from_user.id) + "_about_author")()
        bot.send_message(message.chat.id, message_text)


@bot.message_handler(commands=['about_game'])
def about_game(message: Message):
    if cgs.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    else:
        message_text = getattr(text, cgs.get_user_language(message.from_user.id) + "_about_game")()
        bot.send_message(message.chat.id, message_text)


@bot.message_handler(commands=['new_game'])
def new_game(message: Message):
    if cgs.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    else:
        if cgs.get_user_game_state(message.from_user.id) == states.GAMING:
            message_text = getattr(text, cgs.get_user_language(message.from_user.id) + "_new_game_while_gaming")()
            bot.send_message(message.chat.id, message_text)
        elif cgs.get_user_game_state(message.from_user.id) == states.NONE:
            message_text = getattr(text, cgs.get_user_language(user_id=message.from_user.id) + "_game_rules")()
            cgs.sheet.sheet1.update_cell(row=cgs.get_user_row(user_id=message.from_user.id),
                                         col=cgs.GAME_COL,
                                         value=states.GAMING)
            cgs.sheet.sheet1.update_cell(row=cgs.get_user_row(user_id=message.from_user.id),
                                         col=cgs.GAME_COMBINATION_COL,
                                         value=random_combination())
            cgs.sheet.sheet1.update_cell(row=cgs.get_user_row(user_id=message.from_user.id),
                                         col=cgs.GAME_STEPS_COL,
                                         value=0)
            bot.send_message(message.chat.id, message_text)
        else:
            bot.send_message(message.chat.id, 'Error')


@bot.message_handler(commands=['stop_game'])
def new_game(message: Message):
    if cgs.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    else:
        if cgs.get_user_game_state(user_id=message.from_user.id) == "NONE":
            message_text = getattr(text, cgs.get_user_language(message.from_user.id) + "_cant_end_game")()
            bot.send_message(message.chat.id, message_text)
        elif cgs.get_user_game_state(message.from_user.id) == states.GAMING:
            message_text = getattr(text, cgs.get_user_language(message.from_user.id) + "_ended_game")()
            cgs.sheet.sheet1.update_cell(row=cgs.get_user_row(user_id=message.from_user.id),
                                         col=cgs.GAME_COL,
                                         value=states.NONE)
            cgs.sheet.sheet1.update_cell(row=cgs.get_user_row(user_id=message.from_user.id),
                                         col=cgs.GAME_COMBINATION_COL,
                                         value=states.NONE)
            cgs.sheet.sheet1.update_cell(row=cgs.get_user_row(user_id=message.from_user.id),
                                         col=cgs.GAME_STEPS_COL,
                                         value=states.NONE)
            bot.send_message(chat_id=message.chat.id, text=message_text)
        else:
            bot.send_message(message.chat.id, 'Error')
        # if cgs.get_user_game_state(message.from_user.id) == states.GAMING:
        #     cgs.sheet.sheet1.update_cell(cgs.get_user_row(message.from_user.id), cgs.STATE_COL, states.MAIN_MENU)
        #     cgs.sheet.sheet1.update_cell(cgs.get_user_row(message.from_user.id), cgs.GAME_COL, "NONE")
        #     message_text = getattr(text, cgs.get_user_language(message.from_user.id) + "_ended_game")()
        #     bot.send_message(message.chat.id, message_text)
        # else:
        #     message_text = getattr(text, cgs.get_user_language(message.from_user.id) + "_cant_end_game")()
        #     bot.send_message(message.chat.id, message_text)


@bot.message_handler(content_types=['text'])
def main(message: Message):
    if cgs.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    elif cgs.get_user_game_state(user_id=message.from_user.id) == "gaming" and \
            cgs.get_user_game_combination(user_id=message.from_user.id) != "NONE":
        if RepresentsInt(message.text):
            # len(message.text) == 4:
            # try:
            # guess = int(message.text)
            # bot.send_message(message.chat.id, "Твоя комбинация: " + str(int(message.text)))
            message_out = check_matching(message)
            bot.send_message(message.chat.id, message_out)
            step = cgs.get_user_game_steps(user_id=message.from_user.id) + 1
            cgs.sheet.sheet1.update_cell(cgs.get_user_row(user_id=message.from_user.id), cgs.GAME_STEPS_COL, step)
            if message_out == 'You won!':
                if cgs.get_user_best_score(user_id=message.from_user.id)=='NONE' or step < int(cgs.get_user_best_score(user_id=message.from_user.id)):
                    cgs.sheet.sheet1.update_cell(cgs.get_user_row(user_id=message.from_user.id),
                                                 cgs.BEST_SCORE,
                                                 step)
            # except:
            #     bot.send_message(message.chat.id, "Отправь только свое предположение\nК примеру: 7259")
        else:
            bot.send_message(message.chat.id, "Отправь только свою комбинацюи\nК примеру: 7259")
    else:
        message_text = getattr(text, cgs.get_user_language(message.from_user.id) + "_undefined_text")()
        bot.send_message(message.chat.id, message_text)
        # try:
        #     getattr(states, cgs.get_user_state(message.from_user.id))(message)  # Передает state пользователя
        # except:


def check_matching(message: Message) -> str:
    numbers = list(cgs.get_user_game_combination(user_id=message.from_user.id))
    input_numbers = list(message.text)
    matches = list(set(numbers) & set(input_numbers))
    answer = []
    for x in matches:
        if numbers.index(x) == input_numbers.index(x):
            answer.append('2')
        else: answer.append('1')

    return list_matches_in_answer(matches=answer)


def list_matches_in_answer(matches: list) ->str:
    shuffle(matches)
    answer = ''
    for x in matches:
        if x == '2':
            answer += '⚫'
        elif x == '1':
            answer += '⚪'
    if answer == '⚫⚫⚫⚫':answer = 'You won!'

    return answer


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def random_combination() -> str:
    values = sample(range(1, 6), 4)
    string = ''
    for i in values:
        string += str(i)
    return string

# def list_matches_in_answer(input: list)->str:
#     ans
#     for a in input:


if __name__ == '__main__':
    bot.polling(none_stop=True)
