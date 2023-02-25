# параметры для авторизации
import os
from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_pass = os.getenv('valid_pass')
valid_phone = os.getenv('valid_phone')
valid_login = os.getenv('valid_login')
valid_LC = os.getenv('valid_LC')
test_tel_phone = os.getenv('test_tel_phone')
test_e_mail = os.getenv('test_e_mail')
test_login = os.getenv('test_login')
test_ls = os.getenv('test_ls')
test_pass_word = os.getenv('test_pass_word')