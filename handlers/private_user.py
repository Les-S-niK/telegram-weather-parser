
## Pip modules
from aiogram import Router, types
from aiogram.filters import CommandStart, Command

## Bot modules
from bot_modules.bot_logger import on_message_handler_logger


## Create router for user private channels.
private_user_router: Router = Router(
    name="private_user_router"
)

## Create handlers for other messages and events.

@private_user_router.message(CommandStart())
async def start_command(
    message: types.Message,
) -> None:
    """/start command for telegram bot. Send information about bot.
    
    args:
        message (types.Message): Message object.
    """
    ## Logging the command
    on_message_handler_logger(
        message_text=message.text,
        command_name="start",
        chat_id=message.chat.id,
        username=message.from_user.full_name,
        message_id=message.message_id,
        user_id=message.from_user.id,
        is_bot=message.from_user.is_bot,
    )
    
    ANSWER_TO_START_COMMAND: str = f"""
Hello, {message.from_user.full_name}! 🖐️

I can help you get full information about the weather in the city of interest. 🏙️
To get it, simply write /weather <county name> <city name> that interests you.
🤖 As your assistant, I'll try to send you all the information I have to help you.
"""

    ## Reply to start command.
    await message.reply(
        text=ANSWER_TO_START_COMMAND
    )


@private_user_router.message(Command("help"))
async def help_command(
    message: types.Message
) -> None:
    """Handler of the /help command. Send user help information about using the bot.

    Args:
        message (types.Message): Message object.
    """
    ## Logging the command
    on_message_handler_logger(
        message_text=message.text,
        command_name="help",
        chat_id=message.chat.id,
        username=message.from_user.full_name,
        message_id=message.message_id,
        user_id=message.from_user.id,
        is_bot=message.from_user.is_bot,
    )
    
    ANSWER_TO_HELP_COMMAND: str = f"""
Hi {message.from_user.full_name},
I can tell you the weather when you use the /weather <county> <city> command,
where <county> and <city> is your choose to get information about. 🏙️
"""

    await message.reply(
        text=ANSWER_TO_HELP_COMMAND
    )


@private_user_router.message(Command("weather"))
async def weather_command(
    message: types.Message
) -> None:
    """Handler of the /weather command. Send to user all the information about
    weather in city.

    Args:
        message (types.Message): Message object.
    """
    
    ## Logging the command
    on_message_handler_logger(
        message_text=message.text,
        command_name="weather",
        chat_id=message.chat.id,
        username=message.from_user.full_name,
        message_id=message.message_id,
        user_id=message.from_user.id,
        is_bot=message.from_user.is_bot,
    )
    
    ## Get the city name from used command.
    city_name: str = message.text.replace("/weather", "")
    
    ## TODO: Add parser logic here. 