# Вывести все числа от А до В включительно. А и В - целые, A<=B
a = int(input())
b = int(input())
if a < b:
    step = 1
else:
    step = -1
for i in range(a, b, step):
    print(i, end=' ')
print(b)
