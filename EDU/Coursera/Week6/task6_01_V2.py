def merge(a1, b1):
    c1 = []
    i, j = 0, 0
    while len(c1) < (len(a1) + len(b1)):
        if i >= len(a1):
            c1.append(b1[j])
            j += 1
        elif j >= len(b1):
            c1.append(a1[i])
            i += 1
        elif a1[i] >= b1[j]:
            c1.append(b1[j])
            j += 1
        else:
            c1.append(a1[i])
            i += 1
    return c1


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = merge(a, b)
print(*c)
