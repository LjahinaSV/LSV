f = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025 
k=0

while f>0:
    if f%25 == 0:
        k += 1
    f = f // 25

print(k)
