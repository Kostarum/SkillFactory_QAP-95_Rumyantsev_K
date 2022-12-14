# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать
# общую стоимость билетов. Программа должна работать следующим образом:
#
# 1. В начале у пользователя запрашивается количество билетов,
# которые он хочет приобрести на мероприятие.
#
# 2. Далее для каждого билета запрашивается возраст посетителя,
# в соответствии со значением которого выбирается стоимость:
#
# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате. При этом,
# если человек регистрирует больше трёх человек на конференцию,
# то дополнительно получает 10% скидку на полную стоимость заказа.
num_tikets = int(input("Введите количество билетов, для покупки :"))
age = input("Введите возраст посетителей через пробел :")
list_of_ages = age.split() # список строковых представлений чисел
num_of_ages = list(map(int, list_of_ages)) # список чисел возрастов
price =0
i=0
while i < num_tikets :
    if num_of_ages[i]<18 :
        price += 0
        i+=1
    elif 18<= num_of_ages[i]<= 25:
        price += 990
        i += 1
    else:
        price += 1390
        i += 1
if num_tikets >3:
    print('Сумма к оплате -', price*0.9 ,"рублей")
else:
    print('Сумма к оплате -', price, "рублей")