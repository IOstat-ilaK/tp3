from operator import contains
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command
from filters.chat_types import ChatTypeFilter
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.reply import get_keyboard,del_kb
from database.orm_query import orm_get_products


user_rt=Router()
user_rt.message.filter(ChatTypeFilter(['private']))


@user_rt.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет, я виртуальный помощник",
        reply_markup=get_keyboard(
            "Меню",
            "О нас",
            "Варианты оплаты",
            "Варианты доставки",
            placeholder="Что вас интересует?",
            sizes=(2, 2)
        ),
    )

@user_rt.message(F.text.lower() == 'меню')
@user_rt.message(Command('menu'))
async def menu_cmd(message: types.Message, session:AsyncSession):
    for product in await orm_get_products(session):
        await message.answer_photo(
            product.image,
            caption=f'{product.name}\
            ] \n {product.description}\nСтоимость: {round(product.price,2)}'
        )
    await message.answer("Окак. Вот список товаров")
    await message.answer('Вот твоё меню',reply_markup=del_kb)


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


@user_rt.message(Command("myid"))
async def get_my_id(message: types.Message):
    await message.answer(f"Ваш ID: {message.from_user.id}")


