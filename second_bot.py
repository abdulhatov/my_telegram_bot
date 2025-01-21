import os
from dotenv import load_dotenv
import telebot

load_dotenv()

# Токен бота
TOKEN = os.getenv("TOKEN")

print(TOKEN)

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я простой бот.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "/start - Приветствие\n/help - Список команд\n/about - Информация о боте")

# Обработчик команды /about
@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "Этот бот создан начинающим разработчиком на Python!")

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text.lower() == "привет":
        bot.reply_to(message, "Привет! Чем могу помочь?")
    elif message.text.lower() == "как дела?":
        bot.reply_to(message, "У меня всё отлично, спасибо!")
    else:
        bot.reply_to(message, "Извините, я вас не понял.")

# Запуск бота
bot.polling()