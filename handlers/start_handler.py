from telebot import types
import config


def start(bot, message):
    markup = types.InlineKeyboardMarkup()

    web_app_button = types.InlineKeyboardButton("Старт", web_app=types.WebAppInfo(url=config.URL))
    markup.add(web_app_button)

    bot.send_message(message.chat.id, "Привет!👋 Нажми на кнопку, чтобы открыть приложение.", reply_markup=markup)