#68515 2024
# Определите количество цифр с числовым значением, превышающим 9,
# в 27-⁠ричной записи числа, заданного выражением:

a=2*729**2014+2*81**2018+2*27**2020-2*9**2022-2024
k=0
while a != 0:
    if a%27>9:
        k+=1
    a//=27
print(k)

# 2019
