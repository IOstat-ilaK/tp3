from string import punctuation
from aiogram import F, types, Router
from filters.chat_types import ChatTypeFilter




user_group_rt=Router()
user_group_rt.message.filter(ChatTypeFilter(['group','supergroup']))


restircted_words = {'редиска', 'нехороший человек'}

def clean_text(text:str):
    return text.translate(str.maketrans('','',punctuation))


@user_group_rt.edited_message()
@user_group_rt.message()
async def cleaner(message: types.Message):
    if restircted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f'{message.from_user.username}, имейте совесть!')
        await message.delete()


