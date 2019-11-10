from telebot.types import Message
from random import randint, random, getrandbits, shuffle, sample
import datetime

from bot import bot
import texts.text as text
import states
# import buttons
import config_google_spreadsheet as cgs
import dynamo_db_manage as dbm


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.send_chat_action(action='typing', chat_id=message.from_user.id)
    if dbm.exists(value=message.from_user.id):
        if dbm.get_user_language(message.from_user.id) == "NONE" and (
                message.text != "English" and message.text != "Русский"):
            bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
        else:
            bot.send_message(message.chat.id, getattr(text, dbm.get_user_language(message.from_user.id) + "_user_return")(message.from_user.first_name,))
    else:
        dbm.append_in_table(ID=message.from_user.id,
                            First_Name=message.from_user.first_name,
                            Last_Name=message.from_user.last_name,
                            User_language='NONE',
                            Login='@' + message.from_user.username,
                            Best_score='NONE',
                            Game_comb='NONE',
                            Steps='NONE',
                            Game_status='NONE',
                            Games=0
                            )
        bot.send_message(message.chat.id, text.HELLO_MESSAGE, parse_mode='HTML')
    # if str(message.from_user.id) in cgs.sheet.sheet1.col_values(2):
    #     bot.send_message(message.chat.id, "С возвращением, " + str(message.from_user.first_name) + "!")
    # else:
    #     row = [cgs.get_number_of_rows(cgs.sheet),
    #            message.from_user.id,
    #            message.from_user.first_name,
    #            message.from_user.last_name,
    #            "@" + message.from_user.username,
    #            states.CHOOSE_LANGUAGE,
    #            "NONE",
    #            "NONE",
    #            "NONE",
    #            "NONE",
    #            "NONE"]
    #     cgs.sheet.sheet1.insert_row(row, cgs.get_number_of_rows(cgs.sheet) + 1)
    #     bot.send_message(message.chat.id, text.HELLO_MESSAGE, parse_mode='HTML')


@bot.message_handler(commands=['change_language_to_eng'])
def set_ENG_language(message: Message):
    bot.send_chat_action(action='typing', chat_id=message.from_user.id)
    if dbm.get_user_language(message.from_user.id) == "English":
        bot.send_message(message.chat.id, "This language is already set")
    else:
        dbm.update(user_id=message.from_user.id, item='User_language', new_value='English')
        bot.send_message(message.chat.id, getattr(text, dbm.get_user_language(message.from_user.id) + "_set")())


@bot.message_handler(commands=['change_language_to_rus'])
def set_ENG_language(message: Message):
    bot.send_chat_action(action='typing', chat_id=message.from_user.id)
    if dbm.get_user_language(message.from_user.id) == "Russian":
        bot.send_message(message.chat.id, "Этот язык уже установлен")
    else:
        dbm.update(user_id=message.from_user.id, item='User_language', new_value='Russian')
        bot.send_message(message.chat.id, getattr(text, dbm.get_user_language(message.from_user.id) + "_set")())


@bot.message_handler(commands=['help'])
def help(message: Message):
    bot.send_chat_action(action='typing', chat_id=message.from_user.id)
    if dbm.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    else:
        message_text = getattr(text, dbm.get_user_language(message.from_user.id) + "_help_text")()
        bot.send_message(message.chat.id, message_text,  parse_mode='HTML')


@bot.message_handler(commands=['about_author'])
def about_author(message: Message):
    bot.send_chat_action(action='typing', chat_id=message.from_user.id)
    if dbm.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    else:
        message_text = getattr(text, dbm.get_user_language(message.from_user.id) + "_about_author")()
        bot.send_message(message.chat.id, message_text)


@bot.message_handler(commands=['about_game'])
def about_game(message: Message):
    bot.send_chat_action(action='typing', chat_id=message.from_user.id)
    if dbm.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    else:
        message_text = getattr(text, dbm.get_user_language(message.from_user.id) + "_about_game")()
        bot.send_message(message.chat.id, message_text)


@bot.message_handler(commands=['new_game'])
def new_game(message: Message):
    bot.send_chat_action(action='typing', chat_id=message.from_user.id)
    if dbm.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    else:
        if dbm.get_user_game_state(message.from_user.id) == states.GAMING:
            message_text = getattr(text, dbm.get_user_language(message.from_user.id) + "_new_game_while_gaming")()
            bot.send_message(message.chat.id, message_text)
        elif dbm.get_user_game_state(message.from_user.id) == states.NONE:
            message_text = getattr(text, dbm.get_user_language(user_id=message.from_user.id) + "_game_rules")()
            dbm.update(user_id=message.from_user.id, item='Game_status', new_value=states.GAMING)
            dbm.update(user_id=message.from_user.id, item='Game_comb', new_value=random_combination())
            dbm.update(user_id=message.from_user.id, item='Steps', new_value=str(0))
            bot.send_message(message.chat.id, message_text)
        else:
            bot.send_message(message.chat.id, 'Error')


@bot.message_handler(commands=['stop_game'])
def new_game(message: Message):
    bot.send_chat_action(action='typing', chat_id=message.from_user.id)
    if dbm.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    else:
        if dbm.get_user_game_state(user_id=message.from_user.id) == "NONE":
            message_text = getattr(text, dbm.get_user_language(message.from_user.id) + "_cant_end_game")()
            bot.send_message(message.chat.id, message_text)
        elif dbm.get_user_game_state(message.from_user.id) == states.GAMING:
            message_text = getattr(text, dbm.get_user_language(message.from_user.id) + "_ended_game")()
            dbm.update(user_id=message.from_user.id, item='Game_status', new_value=states.NONE)
            dbm.update(user_id=message.from_user.id, item='Game_comb', new_value=states.NONE)
            dbm.update(user_id=message.from_user.id, item='Steps', new_value=states.NONE)
            bot.send_message(chat_id=message.chat.id, text=message_text)
        else:
            bot.send_message(message.chat.id, 'Error')


@bot.message_handler(commands=['list'])
def list_of_values(message: Message):
    bot.send_chat_action(action='typing', chat_id=message.from_user.id)
    bot.send_message(message.chat.id, str(dbm.get_user_language(message.from_user.id)))


@bot.message_handler(content_types=['text'])
def main(message: Message):
    bot.send_chat_action(action='typing', chat_id=message.from_user.id)
    if dbm.get_user_language(message.from_user.id) == "NONE" and (message.text != "English" and message.text != "Русский"):
        bot.send_message(message.chat.id, text.UNDEFINED_LANGUAGE)
    elif dbm.get_user_game_state(user_id=message.from_user.id) == "gaming" and \
            dbm.get_user_game_combination(user_id=message.from_user.id) != "NONE":
        if RepresentsInt(message.text):
            message_out = check_matching(message)
            bot.send_message(message.chat.id, message_out)
            step = int(dbm.get_user_game_steps(user_id=message.from_user.id)) + 1
            dbm.update(user_id=message.from_user.id, item='Steps', new_value=str(step))
            # cgs.sheet.sheet1.update_cell(cgs.get_user_row(user_id=message.from_user.id), cgs.GAME_STEPS_COL, step)
            if message_out == 'You won!':
                games = int(dbm.get_user_games_number(user_id=message.from_user.id))
                dbm.update(user_id=message.from_user.id, new_value=str(games+1), item='Games')
                dbm.append_game_in_table(ID=message.from_user.id, Game_number=games + 1, Number_of_steps=dbm.get_user_game_steps(user_id=message.from_user.id))
                dbm.update(user_id=message.from_user.id, new_value='NONE', item='Steps')
                dbm.update(user_id=message.from_user.id, new_value='NONE', item='Game_comb')
                dbm.update(user_id=message.from_user.id, new_value='NONE', item='Game_status')

                if str(dbm.get_user_best_score(user_id=message.from_user.id))=='NONE' or step < int(dbm.get_user_best_score(user_id=message.from_user.id)):
                    dbm.update(user_id=message.from_user.id, new_value=str(step), item='Best_score')
                    dbm.update(user_id=message.from_user.id, item='Game_status', new_value=states.NONE)
                    dbm.update(user_id=message.from_user.id, item='Game_comb', new_value=states.NONE)
                    dbm.update(user_id=message.from_user.id, item='Steps', new_value=states.NONE)

        else:
            bot.send_message(message.chat.id, "Отправь только свою комбинацюи\nК примеру: 7259")
    else:
        message_text = getattr(text, dbm.get_user_language(message.from_user.id) + "_undefined_text")()
        bot.send_message(message.chat.id, message_text)
        # try:
        #     getattr(states, cgs.get_user_state(message.from_user.id))(message)  # Передает state пользователя
        # except:


def check_matching(message: Message) -> str:
    numbers = list(dbm.get_user_game_combination(user_id=message.from_user.id))
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
