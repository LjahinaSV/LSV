# Угадай число
inF = open('input.txt', 'r', encoding='utf8')
gS = set(range(1, int(inF.readline().strip()) + 1))
lines = inF.readlines()
tS = set()
for line in lines:
    if list(line.split()) == ['HELP']:
        break
    elif list(line.split()) == ['YES']:
        gS &= tS
        tS = set()
    elif list(line.split()) == ['NO']:
        gS -= tS
        tS = set()
    else:
        tS |= set(map(int, line.split()))
print(*sorted(list(gS)))
inF.close()
