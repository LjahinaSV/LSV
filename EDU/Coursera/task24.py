a = int(input())
b = int(input())
remainder = a % b
yes = 1 - remainder
no = (remainder + b - 1) // b
print('YES' * yes + 'NO' * no)
