import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import sign_gym
from config import TOKEN



bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher()

class Form(StatesGroup):
    name = State()       # Имя пользователя
    date = State()       # Дата тренировки
    time = State()       # Время тренировки
    type = State()       # Тип тренировки


async def main():
    bot = Bot()
    dp = Dispatcher()
    
    dp.include_routers(sign_gym.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())