# создаём класс
class Product:
# создаём приватный метод.
# Метод - это функция, первый атрибут - self

    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

# создаём метод
    def is_available(self):
        return True if self.quantity_in_stock > 0 else False

# создаём экземпляр класса
eggs = Product("eggs", "food", 5)
print(eggs.is_available())
print(eggs.name, eggs.category, eggs.quantity_in_stock)
