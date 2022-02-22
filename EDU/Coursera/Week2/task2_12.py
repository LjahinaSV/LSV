x = int(input())
y = int(input())
n = 1
x1 = float(x)
while x1 < y:
    n += 1
    x1 = x1 + 0.1 * x1
print(n)
