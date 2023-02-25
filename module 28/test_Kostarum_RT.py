# python -m pytest -v --driver Chrome --driver-path chromedriver.exe test_Kostarum_RT.py

import pickle, pytest
from time import sleep
from pages.base_1 import *
from pages.base_2 import CodeForm
from pages.settings import *


# тест_1 - Открытие сайта Ростелекома по ссылке https://lk.rt.ru/
def test_1_screen(selenium):
    form = AuthForm(selenium)
    assert form.logo.text == '© 2023 ПАО «Ростелеком». 18+'

# тест_2 - Открытие сайта Ростелекома по ссылке https://my.rt.ru/ или https://start.rt.ru/ или https://key.rt.ru/
def test_2_screen(selenium):
    form = CodeForm(selenium)
    form.driver.save_screenshot('screen_0.png')
    assert form.code_form.text == 'Авторизация по коду'

# тест_3 - Сохранение скриншота для БАГ 01-репорта.
# Проверка элементов в левом и правом блоке страницы.
@pytest.mark.xfail(reason="Расположение элементов на странице не соответствует ожидаемым требованиям")
def test_3_location_of_page_blocks_screenshot(selenium):
    form = AuthForm(selenium)
    authorization = form.driver.find_element(By.XPATH,"//h1[contains(text(),'Авторизация')]")
    form.driver.save_screenshot('screen_1.png')
    assert form.lk_form.text == authorization.text


# тест_4 - проверка, что Таб "Номер" не существует для БАГ 02-репорта.
@pytest.mark.xfail(reason="Отсутствует Таб 'Номер' на странице авторизации")
def test_4_number(selenium):
    form = AuthForm(selenium)
    form.driver.save_screenshot('screen_2.png')
    assert form.tab_phone.text == 'Номер'
    # чтобы тест проходил, можно изменить проверку:
    # assert form.tab_phone.text == 'Телефон'

# тест_5 - проверка, что по-умолчанию выбран Таб авторизации по телефону
def test_5_tab_phone(selenium):
    form = AuthForm(selenium)
    phone_tab_class = form.tab_phone.get_attribute("class")

    assert phone_tab_class == "rt-tab rt-tab--small rt-tab--active"

# тест_6 - проверка автоматической смены "таб ввода"
def test_6_change_placeholder(selenium):
    form = AuthForm(selenium)
    form.tab_phone.click()
    sleep(1)
    assert form.placeholder.text == 'Мобильный телефон'

    form.tab_mail.click()
    sleep(1)
    assert form.placeholder.text == 'Электронная почта'

    form.tab_login.click()
    sleep(1)
    assert form.placeholder.text == 'Логин'

    form.tab_ls.click()
    sleep(1)
    assert form.placeholder.text == 'Лицевой счёт'

# тест_17 - тест получения временного кода на телефон и открытия формы для ввода кода, позитивный, перемещен сюда,
# чтобы сократить общее время тестов, из за 120 сек задержки запроса на код, т.к. будет еще негативный тест ;)
def test_17_get_code(selenium):
    form = CodeForm(selenium)
    # ввод телефона
    form.address.send_keys(valid_phone)
    form.get_click()
    rt_code = form.driver.find_element(By.ID, 'rt-code-0')
    assert rt_code

# тест_7 - тест перехода на форму регистрации
def test_7_registration(selenium):
    form = AuthForm(selenium)
    # клик по надписи "Зарегистрироваться"
    form.register.click()
    register_form = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    assert register_form.text == 'Регистрация'

# тест_8 - проверка, что кнопки "Продолжить" на форме Регистрации не существует для БАГ-03 репорта.
@pytest.mark.xfail(reason="Отсутствует кнопка 'Продолжить' на странице регистрации")
def test_8_number(selenium):
    form = AuthForm(selenium)
#клик по надписи "Зарегистрироваться"
    form.register.click()
    form.driver.save_screenshot('screen_3.png')
    register_button = form.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/section[2]/div[1]/div[1]/div[1]/form[1]/button[1]')
    assert register_button.text == 'Продолжить'
    # чтобы тест проходил, можно изменить проверку:
    # assert register_button.text == 'Зарегистрироваться'

# тест_9 - позитивный тест авторизации по телефону
def test_9_positive_by_phone(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys(valid_pass)
    form.btn_click()
    # Сохранение cookies браузера после логина
    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(selenium.get_cookies(), cookies)

    assert form.get_current_url() == '/account_b2c/page'

# тест_10 - негативный тест авторизации по телефону
def test_10_negative_by_phone(selenium):
    form = AuthForm(selenium)
    # ввод телефона
    form.username.send_keys(test_tel_phone)
    form.password.send_keys(test_pass_word)
    form.btn_click()
    error_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert error_mess.text == 'Неверный логин или пароль' or  'Неверно введен текст с картинки'

# тест_11 - позитивный тест авторизации по почте
def test_11_positive_by_email(selenium):
    form = AuthForm(selenium)
    # ввод почты
    form.username.send_keys(valid_email)
    form.password.send_keys(valid_pass)
    form.btn_click()
    assert form.get_current_url() == '/account_b2c/page'

# тест_12 - негативный тест авторизации по почте
def test_12_negative_by_email(selenium):
    form = AuthForm(selenium)
    # ввод почты
    form.username.send_keys(test_e_mail)
    form.password.send_keys(test_pass_word)
    form.btn_click()
    error_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert error_mess.text == 'Неверный логин или пароль' or  'Неверно введен текст с картинки'

# тест_13 - позитивный тест авторизации по логину
def test_13_positive_by_login(selenium):
    form = AuthForm(selenium)
    # ввод
    form.username.send_keys(valid_login)
    form.password.send_keys(valid_pass)
    form.btn_click()
    assert form.get_current_url() == '/account_b2c/page'

# тест_14 - негативный тест авторизации по логину
def test_14_negative_by_login(selenium):
    form = AuthForm(selenium)
    # ввод почты
    form.username.send_keys(test_login)
    form.password.send_keys(test_pass_word)
    form.btn_click()
    error_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert error_mess.text == 'Неверный логин или пароль' or  'Неверно введен текст с картинки'

# тест_15 - позитивный тест авторизации по лицевому счету
def test_15_positive_by_LS(selenium):
    form = AuthForm(selenium)
    # ввод лицевого счета
    form.tab_ls_click()
    form.username.send_keys(valid_LC)
    form.password.send_keys(valid_pass)
    form.btn_click()
    assert form.get_current_url() == '/account_b2c/page'

# тест_16 - негативный тест авторизации по лицевому счету
def test_16_negative_LS(selenium):
    form = AuthForm(selenium)
    form.tab_ls.click()
    # ввод почты
    form.username.send_keys(test_ls)
    form.password.send_keys(test_pass_word)
    form.btn_click()
    error_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert error_mess.text == 'Неверный логин или пароль' or  'Неверно введен текст с картинки'




# тест_19 - тест восстановления пароля по номеру телефона
def test_19_forgot_pass_phone(selenium):
    form = AuthForm(selenium)
    # клик по надписи "Забыл пароль"
    form.forgot.click()
    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    user = form.driver.find_element(By.ID, 'username')
    user.send_keys(valid_phone)
    # длительная пауза предназначена для ручного ввода капчи при необходимости
    sleep(25)
    # form.driver.save_screenshot('screen_10.png')
    assert reset_pass.text == 'Восстановление пароля'

# тест_20 - тест восстановления пароля по электронной почте
def test_20_forgot_pass_email(selenium):
    form = AuthForm(selenium)

    # клик по надписи "Забыл пароль"
    form.forgot.click()
    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    user = form.driver.find_element(By.ID, 'username')
    user.send_keys(valid_email)
    # длительная пауза предназначена для ручного ввода капчи при необходимости
    sleep(25)
    # form.driver.save_screenshot('screen_11.png')
    assert reset_pass.text == 'Восстановление пароля'

# тест_18 - тест получения временного кода на телефон и открытия формы для ввода кода, негативный
# с сохранением скриншота в файл screen_4.png, перемещен в самый конец тестов,
# т.к. таймер на 120сек при вводе кода, не дает делать проверку чаще и чтобы не увеличивать общее время тестов.
@pytest.mark.xfail(reason="Сообщение об отсутствии в зарегистрированных этого телефонного номера")
def test_18_get_test_code(selenium):
    form = CodeForm(selenium)
    # ввод телефона
    form.address.send_keys(test_tel_phone)
    # sleep(121)
    form.get_click()
    test_code = form.driver.find_element(By.ID, 'rt-code-0')
    form.driver.save_screenshot('screen_4.png')
    assert test_code