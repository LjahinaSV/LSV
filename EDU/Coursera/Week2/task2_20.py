x = int(input())
y = x
i = 1
tMax = 1
while x != 0:
    x = int(input())
    if x != y:
        if i > tMax:
            tMax = i
        i = 1
        y = x
    else:
        i += 1
print(tMax)
