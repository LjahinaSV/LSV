'''Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
Решите задачу с помощью метода конструктора и примените один из принципов наследования.
При выводе в консоль вы должны получить: «Иван Петров, г. Москва, статус "Наставник"»'''
# по версии на githab https://github.com/expowheella/SkillFactory/tree/master/1.10.4
class GuestsList:
    def __init__(self, full_name, city):
        self.full_name = full_name
        self.city = city

class NewGuests(GuestsList):
    def __init__(self, full_name= '', city= '', status = ''):
        super().__init__(full_name, city)
        self.status = status

    def init_from_dict(self, collection):
        self.full_name = collection.get("full_name")
        self.city = collection.get("city")
        self.status = collection.get("status")

personnel_collection={}
collection = []
a = "N"
while True:
    if a == "N" or a == "n":
        full_name = input('Введите имя: ')
        city = input('Введите город: ')
        status = input('Введите роль сотрудника: ')
        print('Нажмите "Y", если хотите завершить заполнение списка, '
              '"N", если хотите продолжить заполнение')
        personnel_collection['full_name'] = full_name
        personnel_collection['city'] = city
        personnel_collection['status'] = status

        collection.append(personnel_collection.copy()) # !
        a = input()
        continue
    elif a == "Y" or a == "y":
        break

for guest in collection:
    guest_person = NewGuests()
    guest_person.init_from_dict(guest)
    print(f'{guest_person.full_name},', f'г.{guest_person.city},', f'статус "{guest_person.status}"')