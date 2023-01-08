#
a = list(map(int, input().split()))
s = a[0]
n = a[1]
r = []
for i in range(0, n):
    r.append(int(input()))
r.sort()
summa = 0
k = 0
while summa <= s and k < n:
    summa += r[k]
    k += 1
if summa <= s:
    k += 1
print(k-1)
