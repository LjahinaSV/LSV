s = input()
n = s.find(' ')
s1 = s[n + 1:len(s)] + ' ' + s[0:n]
print(s1)
