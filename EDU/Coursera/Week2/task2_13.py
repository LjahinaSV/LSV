n = int(input())
maks = n
while n != 0:
    if n != 0 and n > maks:
        maks = n
    n = int(input())

print(maks)
