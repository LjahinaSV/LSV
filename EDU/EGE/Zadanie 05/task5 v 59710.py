# Задание 5 № 59710
for n in range(4,1000):
    s=format(n, 'b')
    s=str(s)
    if n%3==0:
        s=s+s[-3:]
    elif n%3==1:
        s=s+'11'
    else:
        s=s+'110'
        
    r=int(s, 2)
    if r >=76:
        print(n)
        break
        


        
