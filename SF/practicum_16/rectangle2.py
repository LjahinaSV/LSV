# Исключение при попытке ввести отриц или 0
class NonPositiveDigitException(ValueError):
    pass


from math import pi

# конструктор класса для прямоугольника
class Rectangle:
    def __init__ (self, a,b):
        if a <= 0:
            raise NonPositiveDigitException(f'Неправильно указанна сторона прямоугольника {a}')
        if b <= 0:
            raise NonPositiveDigitException(f'Неправильно указанна сторона прямоугольника {b}')
        self.a = a
        self.b = b
# площадь
    def get_area_rectangle(self):
        return self.a * self.b

# периметр
    def get_perimetr_rectangle(self):
        return 2*(self.a + self.b)

# конструктор класса для квадрата
class Square:
    def __init__ (self, a):
        if a <= 0:
            raise NonPositiveDigitException(f'Неправильно указанна сторона квадрата {a}')
        self.a = a
    def get_area_square(self):
        return self.a **2
    def get_perimetr_square(self):
        return 4*self.a

# конструктор класса для круга
class Circle:
#    def __init__ (self,r,pi=3.1415):
    def __init__(self, r):
        if r <= 0:
            raise NonPositiveDigitException(f'Неправильно указан радиус круга {r}')
        self.r = r
       # self.pi=pi

    def get_area_circle(self):
       # return self.pi*self.r **2
        return pi * self.r ** 2

    def get_circumference_length(self):
        return 2*pi*self.r