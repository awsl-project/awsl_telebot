import logging
import telebot
import requests

from telebot.types import Message
from config import settings
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

bot = telebot.TeleBot(settings.telebot_token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    bot.reply_to(message, "type command se to use")


@bot.message_handler(commands=['se', 'sese', 'awsl'])
def send_awsl(message: Message):
    res = requests.get(settings.url)
    _logger.info("get url: %s - chat_id %s", res.text, message.chat.id)
    bot.reply_to(message, res.text)


@bot.message_handler(commands=['moyu', 'mo', 'moyuban'])
def send_moyu(message: Message):
    res = requests.get(settings.moyu_url)
    bot.reply_to(message, res.text)


_logger.info("start")
bot.infinity_polling()
