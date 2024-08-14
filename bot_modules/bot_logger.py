
## Pip modules
from loguru import logger

## Bot modules.
from config import BOT_NAME, DIR_PATH


## * Create the logger.
logger.add(
    f"{DIR_PATH}/LOGS.log", 
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", 
    rotation="1 MB", 
    compression="zip", 
    level="DEBUG", 
    colorize=True
)

## On start bot logger.
def start_logger() -> None:
    logger.info(
    f"""
    <<< {BOT_NAME} >>>
    < BOT IS ONLINE NOW >
    """
)

## On message bot logger.
def on_message_handler_logger(
    message_text: str,
    command_name: str,
    chat_id: int,
    username: str,
    user_id: int,
    message_id: int,
    is_bot: bool,
) -> None:
    """Message handler logger.

    Args:
        message_text (str): message.text
        command_name (str): Name of the used command.
        chat_id (int): message.chat.id
        username (str): message.from_user.full_name
        user_id (int): message.from_user.id
        message_id (int): message.id
        is_bot (bool): message.from_user.is_bot
    """
    logger.debug(
        f"""
        <<<< {BOT_NAME} >>>>
        Message text: <<{message_text}>>,
        Command name: <<{command_name}>>,
        Chat id: <<{chat_id}>>,
        Username: <<{username}>>,
        User id: <<{user_id}>>,
        Message id: <<{message_id}>>,
        Is bot: <<{is_bot}>> .
        """
    )