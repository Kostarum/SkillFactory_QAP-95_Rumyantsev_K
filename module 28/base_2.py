#Базовый класс
# -*- coding: utf8 -*-
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


class BaseForm(object):
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_base_url(self):
        url = urlparse(self.driver.current_url)
        return url.hostname

# Класс объекта авторизации по коду на телефон или почту
class CodeForm(BaseForm):
    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        # Через Онлайн  Web https://my.rt.ru/
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth/' \
              '?client_id=lk_onlime&redirect_uri=https%3A%2F%2Fmy.rt.ru%2Fauth%2Fssoredirect%2F&response_type=code'

        # Или через Старт Web https://start.rt.ru/
        # url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_decosystems' \
        #       '&redirect_uri=https://start.rt.ru/&response_type=code&scope=openid&theme=light'

        # Или через Ключ  Web https://key.rt.ru/
        # url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_dmh&' \
        #       'redirect_uri=https://sso.key.rt.ru/api/v1/oauth2/b2c/callback&response_type=code&state=' \
        #       'aHR0cHM6Ly9rZXkucnQucnUvbWFpbi9zaWduaW4/dD0xNjc3MjI0NjMyMDU5'

        driver.get(url)

        self.address = driver.find_element(By.ID, "address")
        self.code_btn = driver.find_element(By.ID, "otp_get_code")
        self.logo = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/footer[1]/div[1]/div[1]')
        self.code_form = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[2]/div[1]/div[1]/h1[1]")
        self.auth_form = driver.find_element(By.ID, 'page-right')
        self.lk_form = driver.find_element(By.ID, 'page-left')

    def get_click(self):
        self.code_btn.click()

