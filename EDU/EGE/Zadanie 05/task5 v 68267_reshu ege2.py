# Михаил Глинский
for N in range(100,10000):
    m = []
    s = str(N)
    while len(s) >= 3:
        m.append(int(s[:3]))
        s = s[1:]
    R = max(m) - min(m)
    if R == 623:
        print(N)
        break
