import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from dotenv import load_dotenv
pupils = []
class UserInfo(StatesGroup):
    name = State()
    favorite_language = State()
    expyers=State()


async def start(message: Message) -> None:
    await message.answer("Умники и умницы приветствуют тебя. Как тебя зовут? В каком ты классе? Напиши сво номер телефона, пожалуйста")


async def name(message: Message, state: FSMContext) -> None:
    text=message.text
    pupils.append(text)
    await message.answer("По какой теме у тебя проблема?")
async def my_command(message: Message, state: FSMContext) -> None:
    await message.answer("welcome")


async def main() -> None:
    # переименуй файл .env в .env и подставь соотвествующие данные
    load_dotenv()
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    dp = Dispatcher()
    dp.message.register(my_command, Command("start"))
    dp.message.register(echo, Command('echo'))
    dp.message.register(reverse, Command('reverse'))

    bot = Bot(token=bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    
