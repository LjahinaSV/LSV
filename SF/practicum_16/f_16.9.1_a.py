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

# Позаимствовала и творчески изменила с форума https://python.su/forum/topic/41033/
class Shape:  # конструктор формы
   def to_string(self):
       name = self.__class__.__name__
       attrs = self.__dict__.values()
       return name + '(' + ', '.join(map(str, attrs)) + ')'

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Triangle2D(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

rectangle = Rectangle(5, 10, 50, 100)
print("Прямоугольник: ",rectangle.to_string())
#'Rectangle(5, 10, 50, 100)'

triangle2d = Triangle2D(0, 0, 2, 2, 5, 0)
print("Треугольник на плоскости: ",triangle2d.to_string())
#'Triangle2D(0, 0, 2, 2, 5, 0)'

circle = Circle(1, 1, 15)
print("Окружность: ",circle.to_string())
#'Circle(1, 1, 15)'