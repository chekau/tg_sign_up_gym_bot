import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import sign_gym
from config import TOKEN


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
    dp.include_routers(sign_gym.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())