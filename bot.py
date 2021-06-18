from telebot import TeleBot, types

from now import weather_for_now
from extended_weather import weather_for_next_7_days


TOKEN = '1850062110:AAFJTXGQNF5KsWRcN27-vacqau8vMHG3nAM'
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id,
                     '''Привет! Меня зовут Эдгар. Я погодный-бот.

Ты можешь узнать погоду в Бишкек написав "Сегодня" или "Следующие 7 дней"
или набрав команду /weather''')


@bot.message_handler(commands=['weather'])
def buttons(message):
    markup = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton('Сегодня')
    button_2 = types.KeyboardButton('Следующие 7 дней')
    markup.row(button_1, button_2,)
    bot.send_message(message.chat.id,
                     'Узнать погоду на:',
                     reply_markup=markup)


@bot.message_handler(regexp='сегодня')
def get_weather_for_now(message):
    bot.send_message(message.chat.id, weather_for_now)


@bot.message_handler(regexp='следующие 7 дней')
def get_weather_for_now(message):
    bot.send_message(message.chat.id, weather_for_next_7_days)


@bot.message_handler(content_types=['text'])
def get_weather(message):
    bot.send_message(message.chat.id, '''
Я не знаю что ответить, чтобы узнать погоду нажмите /weather''')


bot.polling()
