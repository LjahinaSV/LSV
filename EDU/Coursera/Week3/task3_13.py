s = input()
n = s.find('f')
if n == -1:
    print(-2)
else:
    n = s.find('f', n + 1)
    print(n)
