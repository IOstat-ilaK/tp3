from string import punctuation
from aiogram import F, types, Router, Bot
from aiogram.filters import Command


from filters.chat_types import ChatTypeFilter
from common.restricted_words import restircted_words




user_group_rt=Router()
user_group_rt.message.filter(ChatTypeFilter(['group','supergroup']))
user_group_rt.edited_message.filter(ChatTypeFilter(['group','supergroup']))

def clean_text(text:str):
    return text.translate(str.maketrans('','',punctuation))

@user_group_rt.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()


@user_group_rt.edited_message()
@user_group_rt.message()
async def cleaner(message: types.Message):
    if restircted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f'{message.from_user.username}, имейте совесть!')
        await message.delete()


