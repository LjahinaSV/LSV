# По данному натуральному n≤9 выведите лесенку из n ступенек,
# i-я ступенька состоит из чисел от 1 до i без пробелов.
n = int(input())
k = 0
s = 0
for i in range(1, n+1):
    k += 1
    s = s * 10 + k
    print(s)
