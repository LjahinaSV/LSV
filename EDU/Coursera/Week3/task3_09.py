# Система линейных уравнений
a, b, c, d, e, f = float(input()), float(input()), float(input()), \
                   float(input()), float(input()), float(input())
x = (e * d - b * f) / (a * d - b * c)
y = (a * f - c * e) / (a * d - b * c)
print(x, y)
