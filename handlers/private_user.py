
## Pip modules
from aiogram import Router, types
from aiogram.filters import CommandStart

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
Hello dear {message.from_user.full_name}! 🖐️

This bot 🤖 can help you to get the weather in your city. 
To get the weather, simply send me a message with your city name.
I'll send you all the information about the weather in your city.
    """

    ## Reply to start command.
    await message.reply(
        text=ANSWER_TO_START_COMMAND
    )
    