# количество цифр в числе 100!
f = 1
i = 1
while i <= 100:
    f *= i
    i += 1
print(f)
print(len(str(f)))
