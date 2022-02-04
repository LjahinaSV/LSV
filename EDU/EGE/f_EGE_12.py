s = '8'*70
print(s, len(s))

while ("2222" in s) or ("8888" in s):
    if "2222" in s:
        s="88"+s[4:]
    elif "22" in s:
        s="2222"+s[6:]
    else: s="22"+s[4:]
    print (s, len(s))