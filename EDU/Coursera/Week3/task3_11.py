s = input()
n1 = s.find('f')
if n1 != -1:
    print(n1, end=' ')
n2 = s.rfind('f')
if n2 != -1 and n1 != n2:
    print(n2)
