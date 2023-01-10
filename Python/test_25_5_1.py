# Множественный поиск элементов с помощью Selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import webbrowser
import time

@pytest.fixture(autouse=True)
def testing():
   # pytest.driver = webdriver.Firefox('C:\geckodriver.exe')
   # pytest.driver.implicitly_wait(10)
   # pytest.driver.get('http://petfriends.skillfactory.ru/login')
   # myDynamicElement = pytest.driver.find_element(By.ID, "pass")

   pytest.driver = webdriver.Chrome('C:\chromedriver.exe')
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   email = pytest.driver.find_element(By.ID, "email")
   yield

   pytest.driver.quit()


def test_login_and_My_pets_content():
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим email
   pytest.driver.find_element(By.ID,'email').send_keys('kostarum@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('qap-95')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
   # Нажимаем на Мои питомцы для входа в личный кабинет
   pytest.driver.find_element(By.XPATH, '//a[contains(text(),"Мои питомцы")]').click()
   # Проверяем, что мы оказались на личной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "Konstantin Rumyantsev"
   time.sleep(2) # Для визуализации страницы "Мои питомцы"

# Пришло время самого интересного: нам нужно взять то множество элементов, которое мы нашли,
# и убедиться, что внутри каждого из них есть имя питомца, возраст и вид.

   My_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
   My_pets_images = pytest.driver.find_elements(By.XPATH, '//tbody/tr/th/img')
   pets_names=[]
   pets_types=[]
   pets_ages=[]


   for pet in My_pets:
      pets_names.append(pet.text.split(' ')[0])
      pets_types.append(pet.text.split(' ')[1])
      pets_ages.append(pet.text.split(' ')[2])
   print(f'Имена питомцев:',pets_names)
   print(f'Количество питомцев',len(pets_names))
   print(f'Порода питомцев:', pets_types)
   print(f'Возраст питомцев:', [x[0] for x in pets_ages])

# Написать тест, который проверяет, что на странице со списком питомцев пользователя:

# 1.Хотя бы у половины питомцев есть фото.
# Количество питомцев с фото тоже можно посчитать, взяв статистику пользователя
   k=0
   for pet in My_pets_images:
         if pet.get_attribute('src') == '':
            k += 1
            print("Нет фото у данного питомца")
   print(f"Число питомцев ,без фото", k)
# 2. Присутствуют  все питомцы.
   # Необходимо собрать в массив имена питомцев
   duplicate_names = set()
   duplicate_types = set()
   duplicate_ages = set()
   pets_names_dupl = set()
   pets_types_dupl = set()
   pets_ages_dupl = set()
   for i in range(len(pets_names)):
      assert pets_names[i] != ''
      print(pets_names[i])
# Проверяем, что у первого питомца есть фото:
      assert My_pets_images[0].get_attribute('src') != ''
# 3.У всех питомцев есть имя, возраст и порода.
      assert pets_types[i] != ''
      print(pets_types[i])


      assert pets_ages[i] != ''
      print(pets_ages[i][0])

# 4.У всех питомцев разные имена.

      if pets_names[i] in duplicate_names:
         pets_names_dupl.add(pets_names[i])
         # print(f'Есть повторяющиеся имена питомцев', pets_names_dupl)
      else:
         duplicate_names.add(pets_names[i])

# 5.В списке нет повторяющихся питомцев. (Сложное задание).
# Повторяющиеся питомцы — это питомцы, у которых одинаковое  имя, порода и возраст.
      if (pets_types[i] in duplicate_types) or  (pets_ages[i][0] in duplicate_ages) :
         # print(f'Есть повторяющиеся породы питомцев', pets_types[i])
         pets_types_dupl.add(pets_names[i])
      #    print(f'Есть повторяющиеся возрасты питомцев', pets_ages[i][0])
         pets_ages_dupl.add(pets_ages[i][0])
      else:
         duplicate_types.add(pets_types[i])
         duplicate_ages.add(pets_ages[i][0])


      if (len(pets_names_dupl)>0) and (len(pets_types_dupl)>0) and (len(pets_ages_dupl)>0):
          print( "Есть повторяющиеся питомцы!", pets_names_dupl, "столько раз: ", len(pets_names_dupl))
      else:
          print('Нет повторяющихся питомцев')