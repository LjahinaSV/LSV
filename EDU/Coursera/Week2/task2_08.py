a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if d >= e:
    (d, e) = (e, d)
if b <= a:
    (a, b) = (b, a)
if c <= b:
    (b, c) = (c, b)
if b <= a:
    (a, b) = (b, a)
if a <= d and b <= e:
    print("YES")
else:
    print("NO")
