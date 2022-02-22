s = input()
n1 = s.find('h')
n2 = s.rfind('h')
print(s[0:n1] + s[n2 + 1:len(s)])
