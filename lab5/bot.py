import os
import telebot
from telebot import types

# Создание бота
TOKEN = '5050129348:AAHotJZgayeneKSOiXAWUSRjQ4P9Xd-aUzQ'

# Сообщения
mes_hello = 'Hello'
mes_photo = 'Вывести картинку'
mes_count = 'Счастливое число'

# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))

# Создание бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Идентификатор диалога
    chat_id = message.chat.id

    # Текст, введенный пользователем, то есть текст с кнопки
    text = message.text

    # Проверка сообщения и вывод данных
    if text == mes_hello:
        bot.send_message(chat_id, "Hello")
    elif text == mes_photo:
        img = open(os.path.join(cur_path, 'for_bot.jpg'), 'rb')
        bot.send_photo(chat_id, img)
    elif text == mes_count:
        bot.send_message(chat_id, "14")
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton(mes_hello)
        itembtn2 = types.KeyboardButton(mes_photo)
        itembtn3 = types.KeyboardButton(mes_count)
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(chat_id, 'Пожалуйста, нажмите кнопку', reply_markup=markup)


bot.infinity_polling()
