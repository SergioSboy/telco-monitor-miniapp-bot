from handlers import start_handler
from telebot import TeleBot
import config

bot = TeleBot(config.TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    start_handler.start(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    callback_handler.callback(bot, call)


if __name__ == '__main__':
    print("Bot is running...")
    bot.polling(none_stop=True)