# Создайте новый проект с необходимыми директориями и файлами.
# Напишите по одному позитивному тесту для каждого метода калькулятора.
# Папку проекта загрузите на GitHub.
# В названии репозитория добавьте номер задания — 19.2.3.
# Ссылку на репозиторий опубликуйте в задании юнита 19.7.2.
import  pytest

from app.Calculator import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding(self):
        assert self.calc.adding(1,1)==2

    def test_subtraction(self):
        assert  self.calc.subtraction(2,1) ==1

    def test_multiply(self):
        assert  self.calc.multiply(2,1) ==2

    def test_division(self):
        assert  self.calc.division(4,2) ==2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1,0)

    def teardown(self):
        print('Выполнение метода Teardown')