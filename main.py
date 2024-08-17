## Built-in modules.
import asyncio

## Pip modules.
## Aiogram
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeDefault
## Other
from dotenv import load_dotenv

## Bot modules
from config import TOKEN, ALLOWED_UPDATES, BOT_COMMANDS
from handlers.private_user import private_user_router
from bot_modules.bot_logger import start_logger


## Load dotenv from .env file.
load_dotenv()

## Create BOT class instance.
bot: Bot = Bot(
    token=TOKEN,
)

## Create Dispatcher class instance.
dispatcher: Dispatcher = Dispatcher()

## Include all bot routers.
dispatcher.include_routers(
    private_user_router
)

## Start function.
async def main() -> None:
    ## Delete old webhook.
    await bot.delete_webhook(
        drop_pending_updates=True
    )
    ## Set bot commands in "menu".
    await bot.set_my_commands(
        commands=BOT_COMMANDS,
        scope=BotCommandScopeDefault()
    )
    ## Polling the bot.
    await dispatcher.start_polling(
        bot,
        allowed_updates=ALLOWED_UPDATES
    )

## Logging the start.
start_logger()
## Turn on the bot.
asyncio.run(main())