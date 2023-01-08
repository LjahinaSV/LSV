# Надо из englishLatin- словаря сделать latinEnglish-словарь, отсортированный
# Дано:
# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa
# Надо:
# 7
# baca - fruit
# bacca - fruit
# malum - apple, punishment
# multa - punishment
# pomum - apple
# popula - apple
# popum - fruit
n = int(input())
latinEnglish = {}
for i in range(n):
    line = input()
    english = line[:line.find('-')].strip()
    latinsStr = line[line.find('-') + 1:].strip()
    latins = map(lambda s : s.strip(), latinsStr.split(','))
    for latin in latins:
        if latin not in latinEnglish:
            latinEnglish[latin] = []
        latinEnglish[latin].append(english)
print(len(latinEnglish))
for latin in sorted(latinEnglish):
    print(latin, '-', ', '.join(sorted(latinEnglish[latin])))