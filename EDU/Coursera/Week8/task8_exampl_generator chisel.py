def genDecDigs(cntDigits, maxDigit):
    if cntDigits > 0:
        for nowDigit in range(maxDigit + 1):
            for tail in genDecDigs(cntDigits - 1, nowDigit):
                yield nowDigit * 10 ** (cntDigits - 1) + tail
    else:
        yield 0


myList = []
for i in genDecDigs(1, 3):
    myList.append(i)
# print(*genDecDigs(1, 3))
print(*myList)
a = list(genDecDigs(2, 5))
print(*a)
