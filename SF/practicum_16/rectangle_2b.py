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

