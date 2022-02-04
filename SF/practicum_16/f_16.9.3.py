""" В проекте «Дом питомца» скоро появится новая услуга: электронный кошелек.
То есть система будет хранить данные о своих клиентах и об их финансовых операциях.
Написать программу, обрабатывающую данные, и на выходе в консоль получить следующее:
Клиент "Иван Петров". Баланс: 50 руб """

# Конструируем класс Клиент-баланс
class Client:
    def __init__(self, client_name, client_balance):
        self.clientl_name = client_name
        self.client_balance = client_balance

    def get_info(self):
        return f'Клиент "{self.clientl_name}".', \
               f'Баланс: {self.client_balance} руб'

# Создадим клиентскую базу Дома питомца
cl1 = Client ("Иван Петров",50)
cl2 = Client ("Пётр Сидоров",100)
cl3 = Client ("Сидор Иванов",45.5)
cl4 = Client ("Анна Бунина",99.99)

# Создадим список
clients = [cl1, cl2, cl3, cl4]

# Распечатаем список
for client in clients:
    print(*client.get_info())

