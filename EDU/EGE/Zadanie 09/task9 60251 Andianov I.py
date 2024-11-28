# 60251 Решение Ильи Андрианова
count = 0
for s in open('60251.txt'):
    M = sorted([int(x) for x in s.split()])
    copies = [x for x in M if M.count(x) == 2]
    if len(copies) == 4:
        if (sum(copies) / len(copies)) < (sum(M) / len(M)):
            count += 1
print(count)
