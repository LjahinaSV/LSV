# print(*map(lambda a, b: int(a != b), input().split(), input().split()))
print(*map(lambda a, b: int(a) ^ int(b), input().split(), input().split()))
