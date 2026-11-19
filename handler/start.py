from aiogram import Router, types
from aiogram.filters import Command
from keyboard.default_keyboard import main_menu

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(text="""Приветствую Вас, я HR-бот Havas

🤖Я:
- расскажу Вам о компании и о преимуществах работы у нас;
- помогу найти актуальные вакансии и заполнить анкету.

_______________________________________

Xush kelibsiz, men HR-bot Havas

🤖Men:
- sizga kompaniya haqida va biz bilan ishlashning afzalliklari haqida gapirib beraman;
- mavjud vakansiyalarni topishga va so'rovnomani to'ldirishga yordam beraman.""",
                         reply_markup=main_menu())