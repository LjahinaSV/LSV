"""Создайте класс любых геометрических фигур,
где на выход мы получаем характеристики фигуры.
Каждый экземпляр должен иметь атрибуты, которые зависят от выбранной фигуры.
 Например, для прямоугольника это будут аргументы x, y, width и height.
Кроме того вы должны иметь возможность передавать эти атрибуты при создании объекта класса.
Создайте метод, который возвращает атрибуты вашей фигуры в виде строки.
Для реализации используйте str.
К примеру, для объекта «прямоугольник»
со значениями атрибутов x = 5, y = 10, width = 50, height = 100,
метод должен вернуть строку Rectangle(5, 10, 50, 100)."""


# строка конструируется через формат
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle({}, {}, {}, {})'.format(self.x, self.y, self.width, self.height)


class Circle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return 'Circle({}, {}, {})'.format(self.x, self.y, self.r)


rect = Rectangle(5, 10, 50, 100)
print(rect)

circle = Circle(2, 7, 10)
print(circle)
