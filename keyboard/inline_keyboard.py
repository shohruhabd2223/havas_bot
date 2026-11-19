from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def about_menu_inline():
    button = InlineKeyboardButton(text="Fullname", callback_data="fullname")
    button2 = InlineKeyboardButton(text="Photo", callback_data="photo")
    button3 = InlineKeyboardButton(text="Job", callback_data="job")
    button4 = InlineKeyboardButton(text="Back", callback_data="back")
    ikm = InlineKeyboardMarkup(inline_keyboard=[[button, button2, button3],
                                                [button4]])
    return ikm


def photo_menu_inline():
    button = InlineKeyboardButton(text="👍 Like", callback_data="like")
    button2 = InlineKeyboardButton(text="👎 Dislike", callback_data="dislike")
    button4 = InlineKeyboardButton(text="Back", callback_data="back_photo")
    ikm = InlineKeyboardMarkup(inline_keyboard=[[button, button2],
                                                [button4]])
    return ikm


def media_menu_inline():
    button = InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/shohruh_abdurahmon/")
    button2 = InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/@Shoxdev")
    button3 = InlineKeyboardButton(text="Telegram", url="https://t.me/shohruh_abdurahmon")
    button4 = InlineKeyboardButton(text="Back", callback_data="back_media")
    ikm = InlineKeyboardMarkup(inline_keyboard=[[button, button2],
                                                [button3],
                                                [button4]])
    return ikm
