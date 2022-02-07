a = int(input())
x1 = a // 1000
x2 = a % 1000 // 100
x3 = a % 100 // 10
x4 = a % 10
b = x4 * 1000 + x3 * 100 + x2 * 10 + x1
print(a - b + 1)
