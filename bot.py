import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "YOUR_BOT_TOKEN"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(
        f"Assalomu alaykum, {user_name}!\n\n"
        "Informatika fani bo'yicha o'quv botiga xush kelibsiz. 🤖\n"
        "Bu yerda siz testlar yechishingiz va dars materiallarini olishingiz mumkin."
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi!")
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
