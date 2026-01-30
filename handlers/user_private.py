from operator import contains
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command
from filters.chat_types import ChatTypeFilter

from keyboards import reply 

user_rt=Router()
user_rt.message.filter(ChatTypeFilter(['private']))

@user_rt.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, Братишь', 
                         reply_markup=reply.start_kb3.as_markup(
                             resize_keyboard = True, 
                             input_field_placeholder="Что вас интересует?"))


@user_rt.message(F.text.lower() == 'меню')
@user_rt.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('Вот твоё меню',reply_markup=reply.del_kb)


@user_rt.message((F.text.lower().contains('оплат')) | (F.text.lower() == 'оплата'))
@user_rt.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.answer('Плотить можна')


@user_rt.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_rt.message(Command('shipping'))
async def delivery_cmd(message: types.Message):
    await message.answer('Есть такое')


@user_rt.message((F.text.lower().contains('нас')) | (F.text.lower() == 'о нас'))
@user_rt.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('Мы крутые')







# @user_rt.message()
# async def echo(message: types.Message):
#     text = message.text
    
#     if text.lower() in [ "привет",
#     "здравствуй",
#     "добрый день",
#     "приветствую",
#     "рад тебя видеть",
#     "салют",
#     "хелло",
#     "добро пожаловать",
#     "моё почтение",
#     "приветики"]:
#         await message.answer('Рад приветствовать вас тут!')
    
#     elif text.lower() in ["пока",
#     "до свидания",
#     "всего хорошего",
#     "увидимся",
#     "до встречи",
#     "счастливо",
#     "прощай",
#     "будь здоров",
#     "до скорого",
#     "чао"]:
#         await message.answer('И вам всего наилучшего!')
    
#     else:
#         await message.reply(message.text)



