import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv 



load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, дегрод')

@dp.message()
async def echo(message: types.Message):
    text = message.text
    
    if text.lower() in [ "привет",
    "здравствуй",
    "добрый день",
    "приветствую",
    "рад тебя видеть",
    "салют",
    "хелло",
    "добро пожаловать",
    "моё почтение",
    "приветики"]:
        await message.answer('Рад приветствовать вас тут!')
    
    elif text.lower() in ["пока",
    "до свидания",
    "всего хорошего",
    "увидимся",
    "до встречи",
    "счастливо",
    "прощай",
    "будь здоров",
    "до скорого",
    "чао"]:
        await message.answer('И вам всего наилучшего!')
    
    else:
        await message.reply(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())