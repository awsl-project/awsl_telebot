import logging
import telebot

from moyu_config import settings
from moyuban import get_moyu_message

_logger = logging.getLogger(__name__)
_logger = logging.Logger(__name__)
_logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
_logger.addHandler(ch)


# 注册 bot
bot = telebot.TeleBot(settings.telebot_token)

for chat_id in settings.chat_ids.split(","):
    bot.send_message(chat_id, get_moyu_message())
