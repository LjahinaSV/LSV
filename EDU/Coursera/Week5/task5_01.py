# Вывести все числа от А до В включительно. А и В - целые, A<=B
a = int(input())
b = int(input())
for i in range(a, b):
    print(i, end=' ')
print(b)
