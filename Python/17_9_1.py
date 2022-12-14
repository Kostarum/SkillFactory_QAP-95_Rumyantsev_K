
# Напишите программу, которой на вход подается последовательность чисел через пробел, а
# также запрашивается у пользователя любое число.
#
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия
# указанному в условии ввода данных.
#
# Далее программа работает по следующему алгоритму:
#
# 1. Преобразование введённой последовательности в список
#
# 2. Сортировка списка по возрастанию элементов в нем(для реализации сортировки определите функцию)
#
# 3. Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а
# следующий за ним больше или равен этому числу.
#
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который
# был рассмотрен в этом модуле.Реализуйте его также отдельной функцией.
#
# Подсказка
# Помните, что у вас есть числа, которые могут не соответствовать заданному условию.В
# этом случае необходимо вывести соответствующее сообщение
#
# Для проверки загрузите полученное решение на GitHub и прикрепите ссылку.

def binary_search(array, element, left, right):
# Функция двоичного поиска индекса соседа снизу от числа, из введенного отсортированного списка
    global midd
    if left > right:  # если левая граница превысила правую,
        return midd-1  # искомый ближайший(снизу) элемент
    middle = (right + left) // 2  # находимо середину
    midd = middle # запоминаем индекс, если элемента нет в списке
    if array[middle] == element:  # если элемент в середине,
        return middle-1  # возвращаем этот индекс минус 1
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

def sorted_array():
# Реализован алгоритм сортировки вставками.
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = x
    print("отсортированный список:", array)
    return array

def changeText(text):
# Функция убирает все знаки препинания, символы,
# буквы и возвращает список, состоящий из цифр текста.
    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        text = text.replace(i, ' ') # Преобразование ошибочного ввода
    return text.split()

numbers = input("Введите числа через пробел от 0 до 99 :")
list_of_numbers = changeText (numbers) # список строковых представлений чисел
array = list(map(int, list_of_numbers)) # список чисел
array_len= len(array)
print("Вы ввели следующие числа", array)

# Обработка исключений:
# Если введено число больше 99 или меньше 0
try:
    for i in range(1, len(array)):
        x = array[i]
        if x > 99 :
            raise ValueError("Вы ввели некорректное число !")
except ValueError as error:
    print("Число вне диапазона !")
else:
    print("Вы ввели правильные числа") #

# Введение числа от пользователя
element = int(input("Введите число, чтобы узнать индекс ближайшего снизу соседа из списка  :"))
# Обработка исключений:
# Неправильный ввод пользователя
try:
     if element > max(array) :
        print("Максимальное число в списке -", max(array))
        raise ValueError("Вы ввели некорректное число !")
except ValueError as error:
    print("Число вне диапазона списка!")
    element > max(array)
else:
    print(f"Вы ищете индекс, ближайшего соседа снизу от числа {element} ") #

# запускаем алгоритм двоичного поиска на левой и правой границе
print("Индекс числа равен: ",binary_search(sorted_array(), element, 1, array_len)) # печатаем индекс "соседа снизу"





