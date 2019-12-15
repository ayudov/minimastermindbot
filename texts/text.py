import random

HELLO_MESSAGE = "<b>Welcome to the MasterMIND game!\n" \
                "Тебя приветствует игра MasterMIND!</b>\n\n" \
                "If you prefer English language:\n/change_language_to_eng\n" \
                "Если предпочитешь русский язык:\n/change_language_to_rus\n\n" \
                "Начать игру: /new_game\n" \
                "Start a game: /new_game\n\n" \
                "<i>For more info: /help\n" \
                "Для большей информации: /help</i>\n"

CHOOSE_LANGUAGE_ENG = "Choose language\n"
LANGUAGE = "English\n"

# NEW_GAME = "New Game"
# CONTINUE = "Continue"
# SETTINGS = "Settings"
# ABOUT = "About"

# ------
# HELLO_MESSAGE_RUS = "Тебя приветствует игра MasterMIND!\n"
CHOOSE_LANGUAGE_RUS = "Выбери язык\n"
LANGUAGE_RUS = "Русский\n"
UNDEFINED_LANGUAGE = "Please, choose language\n" \
                     "Пожалуйста, сначала выбери язык\n\n" \
                     "If you prefer English language:\n/change_language_to_eng\n" \
                     "Если предпочитешь русский язык:\n/change_language_to_rus\n"

# CHOOSE_LANGUAGE = "If you prefer English language: /change_language_to_eng\n" \
#                   "Если предпочитешь русский язык: /change_language_to_rus"

HELP = "For more info: /help\nДля большей информации: /help"


def English():
    return "English"


def Russian():
    return "Russian"


def Russian_set():
    return "Выбран язык: Русский"


def English_set():
    return "Language chosen: English"


def English_main_menu_new_game():
    return "New game"


def English_main_menu_settings():
    return "Settings"


def English_main_menu_about():
    return "About"


def English_about_author():
    return 'Game was made by @AndreyYudov.\n' \
           'Please, write to me with any questions.\n\n' \
           "<i>© Andrii Yudov, 2019</i>"


def English_about_game():
    return '<a href="https://en.wikipedia.org/wiki/Mastermind_(board_game)">' \
           'Link</a> to article on Wiki of a game description.' \
           'For game guide start a new game /new_game'


def English_change_language():
    return "Choose new language"


def English_ended_game():
    return "You have ended the game"


def English_cant_end_game():
    return "You can't end the game because it is not started yet.\n" \
           "Start new game with /new_game"


def Russian_main_menu_new_game():
    return "Новая игра"


def English_new_game_while_gaming():
    return "You can't start a new game, you are already in"


def Russian_about_author():
    return 'Игра была создана @AndreyYudov, по всем вопросам обращайтесь в личные сообщения.\n\n' \
           '<i>© Андрей Юдов, 2019</i>'


def Russian_main_menu_settings():
    return "Настройки"


def Russian_main_menu_about():
    return "Про "


def Russian_change_language():
    return "Выбери новый язык"


def Russian_about_game():
    return '<a href="https://ru.wikipedia.org/wiki/%D0%91%D1%8B%D0%BA%D0%B8_%D0%B8_%D0%BA%D0%BE%D1%80%D0%BE%D0%B2%D1' \
           '%8B">' \
           'Ссылка</a> на статью в Википедии на описание игры.' \
           'Для показа примера игры надо начать игру /new_game'


def Russian_new_game_while_gaming():
    return "Нельзя начать новую игру, ты уже в ней"


def Russian_ended_game():
    return "Ты закончил игру"


def Russian_cant_end_game():
    return "Ты не можешь закончить игру, гра еще не начата.\n" \
           "Начать новую можно /new_game"


def English_help_text():
    return "<b>You can control me by sending these commands:\n\n</b>" \
           "<b>Game:</b>\n" \
           "/new_game - Start new game, current game will be deleted\n" \
           "/stop_game - End current game\n\n" \
           "<b>Language:</b>\n" \
           "/change_language_to_rus - Change game language to Russian\n" \
           "/change_language_to_eng - Change game language to English\n\n" \
           "<b>Other:</b>\n" \
           "/scores - Show top 3\n\n" \
           "<b>Help:</b>\n" \
           "/about_author - Send information about author\n" \
           "/about_game - Send information about game\n"


def Russian_help_text():
    return "<b>Мною можно управлять следующими командами:\n\n</b>" \
           "<b>Игра:</b>\n" \
           "/new_game - Начать новую игру, поточная будет удалена\n" \
           "/stop_game - Закончить поточную игру\n\n" \
           "<b>Язык:</b>\n" \
           "/change_language_to_rus - Сменить язык игры на русский\n" \
           "/change_language_to_eng - Сменить язык игры на английский\n\n" \
           "<b>Другое:</b>\n" \
           "/scores - Показать топ 3\n\n" \
           "<b>Помощь:</b>\n" \
           "/about_author - Информация про автора\n" \
           "/about_game - Информация про игру\n"


def English_undefined_text():
    return "Unknown operation :("


def Russian_undefined_text():
    return "Неизвестная операция :("


def Russian_game_rules():
    return '<a href="https://telegra.ph/Pravila-igry-11-10">Правила и пример игры</a>\n' \
           'Чтобы закончить эту игру: /stop_game (результаты не сохранятся)'
    # return "Русский текст правил игры"


def English_game_rules():
    return '<a href="https://telegra.ph/Rules-of-the-game-11-12">Rules and example of game</a>\n' \
           'To and this game: /stop_game (results will not be saved)'
    # return "English text of game rules"


def Russian_user_return(user_name: str):
    return f'С возвращением, {user_name}!'


def English_user_return(user_name: str):
    return f'Welcome back, {user_name}!'


def English_won():
    return "You won!"


def Russian_won():
    return "Ты выиграл!"


def Russian_send_your_comb():
    return "Отправь только свою комбинацюи\nК примеру: 4261"


def English_send_your_comb():
    return "Send your combination\nFor example: 4261"


def Russian_send_correct_comb():
    return "Отправь комбинацию из 4-х неповторяющихся чисел\nК примеру: 1426"


def English_send_correct_comb():
    return "Send your combination of 4 non-repeating numbers\nFor example: 1426"


def English_get_top_three():
    return "Here top three:"


def Russian_get_top_three():
    return "Топ 3:"


def Russian_name():
    return "Имя:"


def English_name():
    return "Name:"


def Russian_score():
    return "Счет:"


def English_score():
    return "Score:"


def get_random_cat_sticker()-> str:
    cat_stickers = ['CAADAgADjwADGB0GD0ckrhn7ST9JFgQ', 'CAADAgADlAADGB0GD2N0vIBl_YU9FgQ', 'CAADAgADlwADGB0GD925naB2NCtAFgQ',
                    'CAADAgADqAADGB0GDxehuI_QW14IFgQ', 'CAADAgADnQADGB0GD96UPBJ75fcYFgQ', 'CAADAgADrwADGB0GD2lW7liH9bAcFgQ',
                    'CAADAgAD3wADGB0GDzlvNc3zxUjzFgQ', 'CAADAgAD7QUAAj6IGgswPEAoF7rqGhYE', 'CAADAgADCwYAAj6IGgs4SJaIjvmrChYE',
                    'CAADAgAD6AUAAj6IGgujEXZXOspa_BYE', 'CAADAgADQAADl_TGFEvGqiBA4tFuFgQ', 'CAADAgADEgADl_TGFDToiuVXYbgWFgQ',
                    'CAADBAADuwMAAv4zDQZx45Fls0vnIxYE', 'CAADBAAD3gMAAv4zDQYzjmHHTWwZBBYE']
    return random.choice(cat_stickers)


def get_random_cat_gif()-> str:
    cat_gifs = ['CgADBAADvp8AAsIeZAe9NgtsDnLWBRYE', 'CgADAgADiwQAAqcQUUrZ4tPLkcpfPBYE',
                'CgADBAADDp8AApIcZAfiLwYNP1lcCRYE', 'CgADBAAD4rAAArcXZAdi4exB-q1PIRYE', 'CgADBAAD4rAAArcXZAdi4exB-q1PIRYE',
                'CgADBAAD3qAAAtQdZAeDuFOriLJGkRYE']
    return random.choice(cat_gifs)
