# Борис Савельев
for n in range (1000,10000):
    s=str(n)
    n1=s[0]+s[1]+s[2]
    n2=s[1]+s[2]+s[3]
    if (max(int(n1),int(n2))-min(int(n1),int(n2)))==623:
        print(n)
        break
