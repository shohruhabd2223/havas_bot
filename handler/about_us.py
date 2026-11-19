from aiogram import Router, types, F
from aiogram.filters import Command
from keyboard.default_keyboard import main_menu, about_us_menu

router = Router()
image = "https://avatars.mds.yandex.net/get-altay/10648814/2a0000018ce1f23e5c360409c715abb093d3/L_height"


@router.message(F.text == "🏢 Biz haqimizda")
async def filial_command(message: types.Message):
    await message.answer_photo(photo=image,
                               caption="""🌠HAVAS

📌СЕТЬ ДИСКАУНТЕРОВ "У ДОМА"
Мы предлагаем нашим покупателям качественные продукты по выгодной цене. В наших магазинах представлены товары известных мировых и локальных брендов, а также товары собственного производства.""",
                               reply_markup=about_us_menu())


@router.message(F.text == "🔙Назад")
async def filial_command(message: types.Message):
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