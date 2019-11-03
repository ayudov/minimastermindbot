from telebot import types
import texts.text

#  Кнопки для выбора языка

keyboard_choose_lang = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

keyboard_choose_lang.add(types.KeyboardButton(text=texts.text.LANGUAGE),
                         types.KeyboardButton(text=texts.text.LANGUAGE_RUS))

#  Кнопки главного меню
keyboard_main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# keyboard_main_menu.add(types.KeyboardButton(text=texts.text.LANGUAGE),
#                          types.KeyboardButton(text=texts.text.LANGUAGE_RUS))
