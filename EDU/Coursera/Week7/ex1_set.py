mySet = {3, 1, 2}
print(mySet)

firstSet = {1, 2, 1, 3}
secondSet = {3, 2, 1}
print(firstSet == secondSet)

setFromList = set([1, 2, 3])
print(setFromList)
setFromTuple = set((4, 5, 6))
print(setFromTuple)
setFromStr = set("lol")
print(setFromStr)
setFromRange = set(range(2, 22, 3))
print(setFromRange)
setFromMap = set(map(abs, (1, 2, 3, -2, -4)))
print(setFromMap)
setFromSet = set({3, 2, 1})
print(setFromSet)
mixedSet = {1, 3.14, (1, 2, 3), "i have no idea why i'm here"}
print(mixedSet)
print(len(mixedSet))
print(list(mixedSet))
print(tuple(mixedSet))
print(sorted(mySet))
print(str({3, 2, 1}))
mySet1 = {'abba', 'a', 'long string'}
print(', '.join(mySet1))
print(', '.join(sorted(mySet1)))
