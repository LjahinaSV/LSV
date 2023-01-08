# Количество слов в тексте
with open('input.txt', 'r', encoding='utf8') as inF:
    lines = inF.read().split()
print(len(set(lines)))
# print(*set(lines))
