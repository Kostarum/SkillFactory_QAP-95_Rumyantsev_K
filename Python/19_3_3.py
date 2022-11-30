# Задание 19.3.3
# Попробуйте использовать свободное API для написания запросов GET, POST, DELETE, PUT.
# Ваша задача — выполнить все запросы и напечатать при помощи команды print ответы запросов.
#
# Загрузите ваши результаты в юните 7.

# res = requests.get(url, headers=headers, params=params)
# В нашем учебном приложении указан GET-запрос на адрес /api/key,
# но будьте внимательны, он должен отправлять данные не через параметры запроса,
# а через данные в заголовке. Это сделано для большей безопасности вводимых данных,
# так как url ресурса с параметрами сохраняется в истории браузера и его легче отследить.
# Обратите внимание на интересный ход: мы не можем быть уверены,
# что сервер вернёт ответ в формате json,
# поэтому сначала пытаемся декодировать полученные данные как json-строку.
# Если с этим возникают проблемы, то возвращаем ответ обычным текстом.
# Для этого мы можем проверить значение из возвращаемого заголовка.
import os
import json
import requests
# Импортируем авторизационные данные, е-майл, пароль, API ключ
from tests.settings import valid_email, valid_password, valid_auth_key
from requests_toolbelt.multipart.encoder import MultipartEncoder
name = 'Baks'
animal_type = 'CAT, Scottish Fold'
age = '6'
pet_photo='Baks.jpg'

#  GET /api/key
# Вариант передачи параметров при помощи атрибута params не подходит, см. причину выше.
# Когда у вас много параметров, то их удобнее хранить в словаре, а не в длинной строке.
header_1= {'accept': 'application/json','email': valid_email, 'password':valid_password}
res = requests.get("https://petfriends.skillfactory.ru/api/key", headers = header_1)
res_json = json.loads(res.text)
print('\n' ,res_json.values())


# GET /api/pets  Get list of my pets

header_2 = {'accept': 'application/json', 'auth_key': valid_auth_key}
res = requests.get("https://petfriends.skillfactory.ru/api/pets?filter=my_pets", headers = header_2)

if 'application/json' in res.headers['Content-Type']:

    res_json = json.loads(res.content)
    print(res_json)
else:
    res_json = json.loads(res.text)
    print(res_json)

#POST /api/create_pet_simple Add information about new pet without photo
new_pet_simple = {'name': name, 'animal_type':animal_type, 'age':age}
header_3 = {'accept': 'application/json', 'auth_key': valid_auth_key, 'Content-Type': 'multipart/from-data' }
res = requests.post("https://petfriends.skillfactory.ru/api/create_pet_simple", params = new_pet_simple, headers = header_3)
res_json = json.loads(res.text)
print(res_json)

# #POST /api/pets/set_photo/{pet_id} Add photo of pet
# К сожалению запрос выполняется только через функцию MultipartEncoder, т.к. добавление файла(jpg)
# требует библиотеку requests-toolbelt, с преобразованием файла через эту функкцию, иначе ошибка 404.
pet_id = res_json['id']
print(pet_id)
pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
# pet_photo = r'C:\Users\user\PycharmProjects\pythonProject2\Baks.jpg'
print(pet_photo)
new_pet_photo = MultipartEncoder({'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')})
res = requests.post(f"https://petfriends.skillfactory.ru/api/pets/set_photo/{pet_id}",
headers = {'accept': 'application/json', 'auth_key':valid_auth_key, 'Content-Type': new_pet_photo.content_type }, data= new_pet_photo)

print('Ответ сервера на запрос:',res.status_code)

# POST /api/pets  Add information about new pet
# К сожалению запрос выполняется только через функцию MultipartEncoder, т.к. добавление файла(jpg)
# требует библиотеку requests-toolbelt, с преобразованием файла через эту функкцию, иначе ошибка 404.

pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
new_pet = MultipartEncoder({'name': name, 'animal_type':animal_type, 'age':age, 'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')})
header_4 = {'accept': 'application/json', 'auth_key': valid_auth_key, 'Content-Type': new_pet.content_type }
res = requests.post("https://petfriends.skillfactory.ru/api/pets", headers = header_4, data= new_pet)
res_json = json.loads(res.content)
print(res_json)
print('Ответ сервера на запрос:',res.status_code)


# PUT /api/pets/{pet_id} Update information about pet

pet_id= res_json['id']
print(pet_id)
put_pet = { 'name': "BAKS", 'animal_type':"CATS", 'age':"7" }
res = requests.put(f"https://petfriends.skillfactory.ru/api/pets/{pet_id}",
params = put_pet, headers = {'auth_key': valid_auth_key,'accept': 'application/json'})
res_json = json.loads(res.text)
print(res_json)
print('Ответ сервера на запрос:',res.status_code)

# # DELETE /api/pets/{pet_id} Delete pet from database

pet_id= res_json['id']
res = requests.delete(f"https://petfriends.skillfactory.ru/api/pets/{pet_id}",
headers = {'auth_key': valid_auth_key,'accept': 'application/json'})
print('Ответ сервера на запрос:',res.status_code)
print(f'Удалили питомца под номером - {pet_id}')