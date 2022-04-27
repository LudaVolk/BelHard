#bot = telebot.TeleBot("")

import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot('***')

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, я бот знающий погоду во всем мире' + '\n' +
    'Чтобы узнать погоду напишите в чат название любого города\n/help - все команды бота')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/start - запуск бота\n/help - команды бота\nНапишите в чат название города для получения информации о погоде')

@bot.message_handler(content_types=['text'])

def test(message):
    try:
        place = message.text
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d', config_dict)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        t = w.temperature('celsius')
        t1 = t['temp']
        t2 = t['feels_like']
        t3 = t['temp_max']
        t4 = t['temp_min']

        wi = w.wind()['speed']
        humi = w.humidity
        cl = w.clouds
        dt = w.detailed_status
        ti = w.reference_time('iso')
        pr = w.pressure['press']
        vd = w.visibility_distance
        st = w.status


        bot.send_message(message.chat.id, 'В городе ' + str(place) + ' температура ' + str(t1) + ' C' + '\n' +
                         'Максимальная температура ' + str(t3) + 'C' + '\n'+
                         'Минимальная температура ' + str(t4) + 'C' + '\n' +
                         'Ощущается как ' + str(t2) + 'C' + '\n' +
                         'Скорость ветра ' + str(wi) + 'м/с' + '\n' +
                         'Давление ' + str(pr) + 'мм.рт.ст' + '\n' +
                         'Влажность ' + str(humi) + '%' + '\n' +
                         'Видимость ' + str(vd) + 'метров' + '\n'
                         'Статус ' + str(st) + '\n' + str(dt) )

    except:
        bot.send_message(message.chat.id, ' Такой город не найден')
        print(str(message.text), '- не найден')
bot.polling(none_stop=True, interval=0)
