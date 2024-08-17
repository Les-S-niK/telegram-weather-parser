## Built-in modules
from os import getenv
from os.path import dirname

## Pip modules
from aiogram.types import BotCommand


## * CONSTANTS
## Get the TOKEN from .env file. Where "TOKEN" is .env key.
TOKEN: str = getenv("TOKEN")
## Directory work path.
DIR_PATH: str = dirname(__file__)
## Name of the telegram bot.
BOT_NAME: str = "WeatherParserBOT"
## Allowed updates for bot.
ALLOWED_UPDATES: list = [
    "message"
]
## All bot commands.
BOT_COMMANDS: list = [
    BotCommand(
        command="help",
        description="Need a help? This command can help you with using the bot."
    )
]