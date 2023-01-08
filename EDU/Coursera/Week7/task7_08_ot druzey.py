# Эльхан Касымов - учащийся
d = {}
for i in range(int(input())):
    a, b = input().split()
    d[a], d[b] = b, a
print(d[input()])
