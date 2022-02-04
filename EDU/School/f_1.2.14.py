#Дан фрагмент программы:
#a = input(); b = input(); d = input()
#a = float(a)
#b = float(b)
#d = float(d)
#c = a + b; print (a, b, c, end=""); print(d)
#Упростите его, сократив число операторов.
a,b,d=map(float,input("vv 3 chisla cherez probel:  ").split())
print(a,b,a+b,end="    ")
print(d)