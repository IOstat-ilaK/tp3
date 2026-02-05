import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv
from aiogram.fsm.strategy import FSMStrategy

from handlers.admin_private import admin_router
from handlers.user_private import user_rt
from handlers.user_group import user_group_rt

from common.bot_cmd_list import private


load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message','edited_message']

bot = Bot(token=os.getenv('TOKEN'))

admin_id_str = os.getenv('ADMIN_ID', '')
bot.my_admins_list = [int(id.strip()) for id in admin_id_str.split(',') if id.strip().isdigit()]

dp = Dispatcher(fsm_strategy=FSMStrategy.USER_IN_CHAT)
dp.include_router(user_rt)
dp.include_router(user_group_rt)
dp.include_router(admin_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private,scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())