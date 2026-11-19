from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



def main_menu():
    button = KeyboardButton(text="🏢 Biz haqimizda")
    button2 = KeyboardButton(text="💼 Ariza qoldiring")
    button3 = KeyboardButton(text="📞 Kontaktlar")
    button4 = KeyboardButton(text="💬 Qayta aloqa")
    button5 = KeyboardButton(text="🇷🇺/🇺🇿 Cмена языка")
    rkm = ReplyKeyboardMarkup(keyboard=[[button],
                                        [button2],
                                        [button3, button4],
                                        [button5]],
                              resize_keyboard=True)
    return rkm


def about_us_menu():
    button = KeyboardButton(text="🔰 Дискаунтер — это")
    button2 = KeyboardButton(text="📍Ближайший Филиал")
    button3 = KeyboardButton(text="🔙Назад")
    rkm = ReplyKeyboardMarkup(keyboard=[[button, button2],
                                        [button3],],
                              resize_keyboard=True)
    return rkm


def ariza_menu():
    button = KeyboardButton(text="Toshkent")
    button2 = KeyboardButton(text="Сырдарья")
    button3 = KeyboardButton(text="⬅️Orqaga")
    rkm = ReplyKeyboardMarkup(keyboard=[[button, button2],
                                        [button3],],
                              resize_keyboard=True)
    return rkm


