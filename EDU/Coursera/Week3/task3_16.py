# заменить 1 на one
s = input()
while s.find('1') != -1:
    s = s.replace('1', 'one')
print(s)
