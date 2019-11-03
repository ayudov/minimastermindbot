from telebot.types import Message
from telebot import types
from config import bot
import config_google_spreadsheet as cgs
import texts.text as text
import buttons

CHOOSE_LANGUAGE = 'choose_language'
MAIN_MENU = 'main menu'
GAMING = 'gaming'
NONE = 'NONE'


def choose_language(message: Message):
    if message.text == "Русский":
        language = getattr(text, "Russian")()
    else:
        language = getattr(text, message.text)()

    cgs.sheet.sheet1.update_cell(cgs.get_user_row(message.from_user.id, cgs.sheet), cgs.LANGUAGE_COL, language)
    cgs.sheet.sheet1.update_cell(cgs.get_user_row(message.from_user.id, cgs.sheet), cgs.STATE_COL, 'main_menu')
    # buttons.keyboard_main_menu.add(types.KeyboardButton(text=getattr(text, language + '_main_menu_settings')()),
    #                                types.KeyboardButton(text=getattr(text, language + '_main_menu_about')()))
    bot.send_message(message.chat.id, getattr(text, language + '_set')(), reply_markup=buttons.keyboard_main_menu)

# def main_menu(message: Message):
