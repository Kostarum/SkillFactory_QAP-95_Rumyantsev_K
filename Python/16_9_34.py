
class Client:
    def __init__(self, first_name, second_name , city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance
    def get_first_name(self):
        return self.first_name
    def get_second_name(self):
        return self.second_name
    def get_city(self):
        return self.city
    def get_balance(self):
        return self.balance
    def client_info (self):
        print (f' " {self.first_name} {self.second_name}. {self.city}. Баланс : {self.balance} руб. " ')
    # def __str__(self): #второй вариант через функцию __str__
    #     return (f' " {self.first_name} {self.second_name}. {self.city}. Баланс : {self.balance} руб. " ')
    def client_info_min (self):
        return (f' " {self.first_name} {self.second_name}. {self.city}. " ')
client_1 = Client ('Иван', 'Петров', 'Москва',' 50')
client_2 = Client ('Сергей', 'Иванов', 'Омск',' 30')
# client_1.client_info()
# print(client_1) # второй вариант через функцию __str__
clients = [client_1, client_2]
for client in clients:
    print(client.client_info_min())
