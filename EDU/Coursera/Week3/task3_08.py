# kwur
a, b, c = float(input()), float(input()), float(input())
d = b * b - 4 * a * c
if d == 0:
    print(-b / (2 * a))
elif d > 0:
    x1 = (-b - (b * b - 4 * a * c) ** (1/2)) / (2 * a)
    x2 = (-b + (b * b - 4 * a * c) ** (1/2)) / (2 * a)
    if x2 < x1:
        x1, x2 = x2, x1
    print(x1, x2)
else:
    print()
