# Площадь треугольника
a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
sq = (p*(p - a)*(p - b)*(p - c))**(1/2)
print(sq)
