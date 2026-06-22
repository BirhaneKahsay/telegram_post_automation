import os
from telegram import Bot
from config import Settings


async def get_bot_group_id():
    """ Get the bot group id from the environment variable """

    
    settings = Settings()
    # print(f"Using Telegram Bot Token: {settings.TELEGRAM_BOT_TOKEN}")
    # bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

    # updates = await bot.get_updates(timeout=30)

    # if not updates:
    #     raise ValueError("No updates found. Send a message in the group first.")
    # updates[-1].message.chat.id
    return settings.TELEGRAM_CHAT_ID

def load_captions(file_path: str) -> list:
    """ Load captions from a text file and return them as a list """
    if not os.path.exists(file_path):
        return ["እንኳን ደህና መጡ! ቲሸርቶቻችንን ይመርጡ!"]
    with open(file_path, 'r', encoding='utf-8') as f:
        captions = f.read()
    return captions

def get_bot()-> Bot:
    """ Get the bot instance """
    settings = Settings()
    return Bot(token=settings.TELEGRAM_BOT_TOKEN)

def get_facebook_credentials():
    """ Get Facebook page credentials from environment variables """
    settings = Settings()
    return settings.FACEBOOK_PAGE_ID, settings.FACEBOOK_PAGE_ACCESS_TOKEN