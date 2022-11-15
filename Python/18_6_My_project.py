# 1.Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
# 2.При написании бота необходимо использовать библиотеку pytelegrambotapi.
# 3.Человек должен отправить сообщение боту в виде <имя валюты цену которой он хочет узнать>
# <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>.
# При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
# При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
# Для взятия курса валют необходимо использовать API и отправлять к нему запросы с помощью библиотеки Requests.
# Для парсинга полученных ответов использовать библиотеку JSON.
# При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число)
# вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
# Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.
# Для отправки запросов к API описать класс со статическим методом get_price(),
# который принимает три аргумента: имя валюты, цену на которую надо узнать,
# — base, имя валюты, цену в которой надо узнать, — quote, количество переводимой валюты — amount
# и возвращает нужную сумму в валюте.
# Токен telegramm-бота хранить в специальном конфиге (можно использовать .py файл).
# Все классы спрятать в файле extensions.py.

import telebot
from extensions import keys, TOKEN
from utils import ConvertionExeption, CryptoConverter

bot = telebot.TeleBot(TOKEN)

# обработчик команд для бота
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту, в следующем формате: \n<имя валюты>\
    <в какую валюту перевести> \
    <количество переводимой валюты>\n Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text )

# обработчик ввода пользователя
@bot.message_handler(commands=['values'])
def values (message: telebot.types.Message):
    text = 'Доступные валюты : '
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message,text)

# Функция конвертации валют
@bot.message_handler(content_types =['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        # Проверяем, что введенных слов от пользователя, не более 3х:
        if len(values) != 3:
            raise ConvertionExeption('Слишком много параметров!')
        quote, base, amount = values
        # Вызываем функцию обработчика ввода
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} - {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)
#запуск бота
bot.polling(none_stop=True)