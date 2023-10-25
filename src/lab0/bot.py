import requests
import telebot

bot = telebot.TeleBot('6567134779:AAFtpY5Y1kQWnzboofDlD9D8khKqo_3oC98')

@bot.message_handler()
def get_weather(message):

    
    if (message.text == 'start' or message.text == '/start'):
        bot.send_message(message.chat.id, 'Введите название города и я отправлю вам сводку по погоде!')
    else:
        print(message.text.lower())
        try:
            r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + message.text.lower() + "&appid=fe12e0e4ea3581a740dacc944380c6fe&units=metric&lang=ru")
            data = r.json()

            city_name = data['name']
            real_temp = data['main']['temp']
            feeling = data['main']['feels_like']
            win = data['wind']['speed']
            hum = data['main']['humidity']
            press = data['main']['pressure']
            bot.send_message(message.chat.id,
            f'Погода в городе: {city_name}\nТемпература: {real_temp} C°\nОщущается как: {feeling} C°\n'
            f'Ветер: {win} м/c\nВлажность: {hum} %\nДавление: {press} мм.рт.ст\nХорошего вам дня!'
            )
        except:
            bot.send_message(
                message.chat.id,
                f'Проверьте коректность запроса и вводите только полное название города'
            )

bot.polling(none_stop=True)