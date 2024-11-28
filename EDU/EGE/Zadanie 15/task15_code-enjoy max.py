def F(a, b, x):
    if a <= x <= b:
        return True
    else:
        return False

def F2(a, b, x):
    if a < x < b:
        return True
    else:
        return False

mx=0

for a in range(0, 100):
    for b in range(a, 100):
        k=0
        for i in range(2, 200):
            x=i/2
            if (not(F2(a, b, x)) or F(43, 49, x)) or F(44, 53, x):
                k=k+1

        if k==198:
            mx=max(mx, b-a)
print(mx)
