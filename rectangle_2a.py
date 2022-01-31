# Задание 16.8.2 Полиморфизм
from rectangle2 import Rectangle, Square, Circle

r1 = Rectangle(12,5)
print("Площадь прямоугольника=",r1.get_area_rectangle(),
              " Периметр прямоугольника=", r1.get_perimetr_rectangle())

sq1 = Square(12)
print("Площадь квадрата=", sq1.get_area_square(),
      " Периметр квадрата=", sq1.get_perimetr_square())

cir1 = Circle(10)
print("Площадь круга=", "{:8.4f}".format(cir1.get_area_circle()),
              " Длина окружности=", "{:8.4f}".format(cir1.get_circumference_length()))

r2 = Rectangle(6,8)
sq2 = Square(6)
cir2 = Circle(6)

print('')
print("Использование функции isinstance:")
figures = [r1, sq1, cir1, r2, sq2, cir2]
for figure in figures:
    if isinstance(figure, Rectangle):
        print("Площадь прямоугольника=",figure.get_area_rectangle(),
              " Периметр прямоугольника=", figure.get_perimetr_rectangle())
    elif isinstance(figure, Square):
        print("Площадь квадрата=", figure.get_area_square(),
              " Периметр квадрата=", figure.get_perimetr_square())
    else:
        print("Площадь круга=", "{:8.4f}".format(figure.get_area_circle()),
              " Длина окружности=",  "{:8.4f}".format(figure.get_circumference_length()))


