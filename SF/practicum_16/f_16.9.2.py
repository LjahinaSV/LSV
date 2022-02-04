"""Напишите код для описания геометрической фигуры.
Создайте класс «прямоугольник» с помощью метода  __init__().
 На выходе в консоли вам необходимо получить длину и ширину
 с итоговыми значениями/
 Что такое с итоговыми значениями? И причём тут площадь?"""


class Rectangle:

    def __init__(self, dl, w):
        self.length = dl
        self.width = w

    def rectangle_area(self):
        return self.length*self.width


newRectangle = Rectangle(12, 10)
print("Прямоугольник: длина=", newRectangle.length, ', ширина=', newRectangle.width)
