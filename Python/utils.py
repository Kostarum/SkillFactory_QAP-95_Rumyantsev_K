# Здесь собраны классы обработчиков ошибок
import requests
import json
from extensions import keys

#Создали класс обработчика ошибок
class ConvertionExeption(Exception):
    pass
# Создаем класс обработчика ошибок ввода
class CryptoConverter:
    @staticmethod
    def convert(quote : str, base: str, amount: str):
        # Проверяем, что введенные валюты разные:
        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base} .')
        # Проверяем ввод правильного названия валюты, которую хотим конвертировать
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')
        # Проверяем ввод правильного названия валюты, в которую хотим конвертировать
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')
        # Проверяем, что введено валидное количество валюты :
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')
        # Запрос в CryptoCompare.com - ресурс где можно получить доступ к API сайта с криптовалютами
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        # Переводим полученный формат json в тип словарь для Питона:
        total_base = json.loads(r.content)[keys[base]]*amount
        return total_base
