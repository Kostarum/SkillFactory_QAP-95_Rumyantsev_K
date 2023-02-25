#Базовый класс для автотестов

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

# Класс объекта стандартной авторизации по Телефону, Почте, Логину и Лицевому счету
class AuthForm(BaseForm):
    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        # Через ЕЛК Web , т.к. поддерживает все виды аутентификации
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2' \
              'c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid& '
        driver.get(url)

        self.username = driver.find_element(By.ID, "username")
        self.password = driver.find_element(By.ID, "password")
        self.auth_btn = driver.find_element(By.ID, "kc-login")
        self.tab_phone = driver.find_element(By.ID, 't-btn-tab-phone')
        self.tab_mail = driver.find_element(By.ID, 't-btn-tab-mail')
        self.tab_login = driver.find_element(By.ID, 't-btn-tab-login')
        self.tab_ls = driver.find_element(By.ID, 't-btn-tab-ls')
        self.forgot = driver.find_element(By.ID, "forgot_password")
        self.register = driver.find_element(By.ID, 'kc-register')
        self.logo = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/footer[1]/div[1]/div[1]')
        self.placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
        self.agree = driver.find_element(By.ID, "rt-footer-agreement-link")
        self.auth_form = driver.find_element(By.ID, 'page-right')
        self.lk_form = driver.find_element(By.ID, 'page-left')

    def btn_click(self):
        self.auth_btn.click()

    def tab_phone_click(self):
        self.tab_phone.click()

    def tab_mail_click(self):
        self.tab_mail.click()

    def tab_login_click(self):
        self.tab_login.click()

    def tab_ls_click(self):
        self.tab_ls.click()

    def find_element(self, by, location):
        return self.driver.find_element(by, location)

    def get_current_url(self):
        url = urlparse(self.driver.current_url)
        return url.path




