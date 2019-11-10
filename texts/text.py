HELLO_MESSAGE = "<b>Welcome to the MasterMIND game!\n" \
                "Тебя приветствует игра MasterMIND!</b>\n\n" \
                "If you prefer English language: /change_language_to_eng\n" \
                "Если предпочитешь русский язык: /change_language_to_rus\n\n" \
                "<i>For more info: /help\n" \
                "Для большей информации: /help</i>"
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
    return "English text about author"


def English_about_game():
    return "English text about game"


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
    return "Русский текст про автора"


def Russian_main_menu_settings():
    return "Настройки"


def Russian_main_menu_about():
    return "Про "


def Russian_change_language():
    return "Выбери новый язык"


def Russian_about_game():
    return "Русский текст про игру"


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
           "<b>Помощь:</b>\n" \
           "/about_author - Информация про автора\n" \
           "/about_game - Информация про игру\n"


def English_undefined_text():
    return "Unknown operation :("


def Russian_undefined_text():
    return "Неизвестная операция :("


def Russian_game_rules():
    return "Русский текст правил игры"


def English_game_rules():
    return "English text of game rules"


def Russian_user_return(user_name: str):
    return f'С возвращением, {user_name}!'


def English_user_return(user_name: str):
    return f'Welcome back, {user_name}!'
