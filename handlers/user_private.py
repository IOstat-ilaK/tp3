from aiogram import types, Router
from aiogram.filters import CommandStart, Command


user_rt=Router()



@user_rt.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, дегрод')

@user_rt.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('Держи меню')




@user_rt.message()
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