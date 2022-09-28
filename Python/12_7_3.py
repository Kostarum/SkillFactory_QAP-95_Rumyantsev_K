# Вам дан словарь per_cent с распределением процентных ставок по вкладам
# в различных банках таким образом, что ключ — название банка, значение — процент.
# Напишите программу, в результате которой будет сформирован список
# deposit значений — накопленные средства за год вклада в каждом из банков.
# На вход программы с клавиатуры вводится сумма money, которую человек планирует положить под проценты.
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
cents= list(per_cent.values())# перевод значений словаря в переменную списка
keys = list(per_cent.keys())# перевод ключей словаря в переменную списка
print('Возможные проценты по вкладам -', cents)
print('Банки работающие по вкладам -', keys)
money = int(input("Введите сумму вклада, не менее 100 :"))
# цикл перебора значений списка процентов по вкладам, с поиском максимального
num1=0
for num in cents:
        if num>num1 :
            num1 = num
else:
    deposit_max = num1*money/100
print('Максимальная сумма, которую можете заработать - ', deposit_max)
# цикл формирования списка накоплений в банках
deposit = list()
for num2 in cents:
    all_deposits = deposit.append(num2*money/100+money)
print(deposit , ' — накопленные средства за год по вкладам')
# Для самостоятельного изучения вам была дана ссылка на методы для работы со списками.
# Изучите методы и найдите тот, который позволяет найти максимальное значение среди элементов в списке.
deposit=sorted(deposit)
print(deposit[-1], '— Максимальная сумма, которую можете накопить' )
# Добавьте в программу поиск максимального значения и его вывод на экран в формате:
# Максимальная сумма, которую вы можете заработать — deposit[i]
# Где вместо deposit[i] будет выведено максимальное значение списка.