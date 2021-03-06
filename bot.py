import telebot
from translator import TranslatorCore

bot = telebot.TeleBot("TOKEN")
translator = TranslatorCore()

@bot.message_handler(content_types=['text'])
def send_translate(message):
    text = translator.translate(message.text)
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)