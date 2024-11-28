def F(a, b, x):
    if a<=x<=b:
        return True
    else:
        return False

mn=10**10
for a in range(0, 100):
    for b in range(a, 100):
        k=0
        for i in range(2, 200):
            x = i / 2
            if not(F(15, 40, x)) or (not(F(21, 63, x) and not(F(a, b, x))) or not(F(15, 40, x))):
                k=k+1

        if k==198:
            mn = min(mn, b-a)
            a1=a
            b1=b
            print(mn," [",a1,";",b1,"]")

print(mn)
