import telebot
from config import API_TOKEN
from telebot.types import (KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove,
                           Message)


keyboard = ReplyKeyboardMarkup()
button = KeyboardButton(text="Моя кнопка", request_location=True)
button2 = KeyboardButton(text="Моя кнопка 2")
# button3 = KeyboardButton(text="Моя кнопка 3")
keyboard.add(button)
keyboard.add(button2)
keyboard.add('1', '2')
# keyboard.row('5', '6', '7')


bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    hello_message = f'Приветствую! <b>{message.from_user.username}</b>!!!'
    bot.send_message(
        message.chat.id,
        hello_message,
        reply_markup=keyboard,
        parse_mode='HTML' #  Строка сообщения парсится, как html
    )

@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    if message.text == "Моя кнопка":
        bot.send_message(
            message.from_user.id,
            'Ты нажал кнопку 1',
            reply_markup=ReplyKeyboardRemove()
        )
    elif message.text == "Моя кнопка 2":
        bot.send_message(
            message.from_user.id,
            'Ты нажал кнопку 2',
            reply_markup=keyboard
        )
    else:
        bot.send_message(
            message.from_user.id,
            'Ты нажал не то'
        )

bot.infinity_polling()
