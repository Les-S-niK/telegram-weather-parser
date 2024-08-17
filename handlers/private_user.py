
## Pip modules
from aiogram import Router, types
from aiogram.filters import CommandStart, Command

## Bot modules
from bot_modules.bot_logger import on_message_handler_logger
from bot_modules.weather_parser import WeatherParser


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
    
    ## Fetch city and country name from command text.
    message_text: str = message.text
    ## Split country and city name in text.
    ## I get this list: ["/weather", "County", "City"]
    splited_text: list = message_text.split(sep=" ")
    ## Get county by 1 list index:
    country: str = splited_text[1]
    ## Get city by 2 list index:
    city: str = splited_text[2]

    ## Initialize WeatherParser
    weather_parser: WeatherParser = WeatherParser(
        country=country,
        city=city
    )
    ## Get structured weather information:
    weather_info: dict = weather_parser.weather_information
    ## Fetch all the dict data to variables.
    tempetarure: str = weather_info.get("temp")
    pressure: str = weather_info.get("pressure")
    humidity: str = weather_info.get("humidity")
    max_wind: str = weather_info.get("max_wind")
    cloudness: str = weather_info.get("cloudness")
    visibility: str = weather_info.get("visibility")
    uv_index: str = weather_info.get("uv_index")
    ## Fetch username.
    username: str = message.from_user.full_name
    ## Structuring the answer to user.
    answer_to_user: str = f"""
        {username} here weather information in {city}.
        Temperature: {tempetarure}
        Pressure: {pressure}
        Humidity: {humidity}
        Max wind speed: {max_wind}
        Cloudness: {cloudness}
        Visibility: {visibility}
        UV index: {uv_index}
        """
    ## Send answer to user.
    await message.reply(
        text=answer_to_user
    )