n = int(input())
x = float(input())
p = 0
while n > 0:
    p = (p + float(input())) * x
    n -= 1
print(p + float(input()))
