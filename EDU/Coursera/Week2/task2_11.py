n = int(input())
d = 1
r = 1
while r != 0:
    d += 1
    r = n % d
print(d)
