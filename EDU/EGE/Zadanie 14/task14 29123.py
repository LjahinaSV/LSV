# 29123
''' Сколько "1" в двоичной записи выражения 8**5+4**6+2**12-16 ?
'''
x=8**5+4**6+2**12-16
p=2
s=''
while x !=0:
    s=str(x%p)+s
    x//=p
print(s.count('1'))

# 10
x=8**5+4**6+2**12-16
print(x)
print(bin(x))
print(str(bin(x)[2:].count('1')))
print(oct(x)) # 8 cc
print(hex(x)) # 16 cc
