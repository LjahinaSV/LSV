# Выведите все числа, которые входят как в первый,
# так и во второй список, в порядке возрастания
print(*sorted(set(list(map(int, input().split()))) &
              set(list(map(int, input().split())))))
