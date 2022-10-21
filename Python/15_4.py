
# Напишите программу, которая получает от пользователя имя файла,
# открывает этот файл в текущем каталоге, читает его и выводит два слова:
# наиболее часто встречающееся из тех, что имеют размер более трех символов,
# и наиболее длинное слово на английском языке.
#
# В файле ожидается смешанный текст на двух языках — русском и английском.
#
# name_file = str(input("Введите имя файла на английском языке, и его тип :"))
# print(name_file)
# print(type(name_file))
#
# def changeText(text):
#     """
#     Функция принимает строку с текстом.
#     Убирает все знаки препинания и возвращает
#     список, состоящий из слов текста.
#     """
#
#
#     for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
#         text = text.replace(i, '')
#
#     return text.split()
#
#
# def mostCommon(text, length=0):
#     """
#     Функция принимает список и ограничение по длине.
#     Возвращает самый часто встречающийся элемент.
#     Если есть несколько элементов с одинаковой самой большой частотой, то вернёт их все.
#     """
#
#
#     most_common = []
#     qty_most_common = 0
#
#     for item in text:
#         if len(item) > length:
#             qty = text.count(item)
#             if qty > qty_most_common and qty > 2:
#                 qty_most_common = qty
#                 most_common = [item]
#             elif qty == qty_most_common:
#                 most_common.append(item)
#
#     return list(set(most_common))
#
#
# def mostLength(text):
#     """
#     Функция принимает список.
#     Возвращает самый длинный элемент.
#     Если есть несколько элементов с одинаковой самой большой длиной, то вернёт их все.
#     """
#
#
#     most_length = []
#     qty_most_length = 0
#     alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for item in text:
#         for char in item:
#             if char not in alphabet:
#                 charEn = False
#             else:
#                 charEn = True
#
#         if charEn:
#             qty = len(item)
#             if qty > qty_most_length:
#                 qty_most_lenght = qty
#                 most_lenght = [item]
#             elif qty == qty_most_length:
#                 most_length.append(item)
#
#         return list(set(most_length))
#
# nameFile = input('Название файла: ')
#
# with open(nameFile, encoding='utf8') as f:
#     fileText = f.read()
#
# fileText = changeText(fileText)
# print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 3)}')
# print(f'Список самых длинных английских слов: {mostLength(fileText)}')

# Задание на автоматизацию проверки ответа API от сервера.
#
# У вас есть следующие требования к ответу:

# timestamp: int
# referer: string (url)
# location: string (url)
# remoteHost: string
# partyId: string
# sessionId: string
# pageViewId: string
# eventType: string (itemBuyEvent или itemViewEvent)
# item_id: string
# item_price: int
# item_url: string (url)
# basket_price: string
# detectedDuplicate: bool
# detectedCorruption: bool
# firstInSession: bool
# userAgentName: string
# Вот здесь можно взять пример JSON с ответами некоего интернет-магазина, составленный по этим правилам.
#
# [{"timestamp": 1555296301000, "referer": "https://b24-d2wt09.bitrix24.shop/katalog/item/dress-spring-ease/",
# "location": "https://b24-d2wt09.bitrix24.shop/",
# "remoteHost": "test0", "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",

# Вам нужно написать простой тест, который проверяет JSON на правильность полей. То есть проверяет, что каждый объект в JSON:
#
# Содержит все перечисленные в требованиях поля.
# Не имеет других полей.
# Все поля имеют именно тот тип, который указан в требованиях:
# int — целое число;
# string — произвольная строка;
# string (url) — это строка с url. В рамках этого задания проверяем, что url начинается c http:\\ или https:\\;
# string (itemBuyEvent или itemViewEvent) — строка, в которой могут быть только эти конкретные два значения и никакие другие;
# bool — булево значение, то есть True или False.
# Тест должен вернуть Pass или список значений, которые тест посчитал ошибочными, и причину, почему они ошибочные.

import json
with open('json_example_QAP.json', encoding='utf8') as f:
    templates = json.load(f)
def CheckInt(item):
    return isinstance(item, int)
def CheckStr(item):
    return isinstance(item, str)
def CheckBool(item):
    return isinstance(item, bool)
def CheckUrl(item):
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False
def CheckStrValue(item, val) :
    if isinstance(item,str):
        return item in val
    else:
        return  False
def ErrorLog(item, value, string):
    Error.append({item: f'{value}, {string}'})
listofItems = {'timestamp': 'int', 'item_price': 'int', 'referer': 'url', 'location': 'url', 'item_url': 'url',
               'remoteHost' : 'str','partyID': 'strb', 'sessionId': 'str', 'pageViewId': 'str', 'item_id': 'str',
               'basket_price': 'str', 'userAgentName': 'str', 'eventType': 'val', 'detectedDuplicate': 'bool',
               'detectedCorruption': 'bool', 'firstSession': 'bool'}
Error = []
for items in templates:
    for item in items:
        if item in listofItems:
            if listofItems[item] == 'int':
                if not CheckInt(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}' )
            elif listofItems[item] == 'str':
                if not CheckStr(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}' )
            elif listofItems[item] == 'bool':
                if not CheckBool(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}' )
            elif listofItems[item] == 'url':
                if not CheckUrl(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}' )
            elif listofItems[item] == 'val':
                if not CheckStrValue(items[item], ['itemBuyEvent', 'itemVeewEvent']):
                    ErrorLog(item, items[item], 'ожидали значение itemBuyEvent или itemViewEvent' )
            else:
                ErrorLog(item, items[item], 'неожиданное значение')
        else:
            ErrorLog(item, items[item], 'неизвестная переменная')
if Error == []:
    print('Pass')
else:
    print('Fail')
    print(Error)
