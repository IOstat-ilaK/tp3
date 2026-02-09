import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.fsm.strategy import FSMStrategy

from dotenv import find_dotenv, load_dotenv
from middlewares import db

load_dotenv(find_dotenv())

from handlers.admin_private import admin_router
from handlers.user_private import user_rt
from handlers.user_group import user_group_rt

from database.engine import create_db, drop_db, session_maker

from common.bot_cmd_list import private


ALLOWED_UPDATES = ['message','edited_message']

bot = Bot(token=os.getenv('TOKEN'))

admin_id_str = os.getenv('ADMIN_ID', '')
bot.my_admins_list = [int(id.strip()) for id in admin_id_str.split(',') if id.strip().isdigit()]

dp = Dispatcher(fsm_strategy=FSMStrategy.USER_IN_CHAT)




dp.include_router(user_rt)
dp.include_router(user_group_rt)
dp.include_router(admin_router)



async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()
    
    await create_db()

async def on_shutdown(bot):
    print('Бот упал')




async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(db.DataBaseSession(session_pool=session_maker))
    await create_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private,scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

asyncio.run(main())