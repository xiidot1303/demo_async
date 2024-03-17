from telegram import Bot
from telegram.ext import Dispatcher, PicklePersistence
from telegram.ext import Updater
from bot.control.handlers import handlers
from config import BOT_API_TOKEN, DEBUG


def run_bot(bot_token):
    persistence = PicklePersistence(filename=f"persistencebot{bot_token}")
    bot_obj = Bot(bot_token)

    if not DEBUG:  # in production
        updater = 1213
        dp = Dispatcher(bot_obj, None, workers=1000, use_context=True, persistence=persistence)

    else:  # in development
        updater = Updater(
            token=BOT_API_TOKEN, workers=1000, use_context=True, persistence=persistence,
        )
        dp = updater.dispatcher


    # add handlers
    for handler in handlers[::-1]:
        dp.add_handler(handler)
    return dp, updater
