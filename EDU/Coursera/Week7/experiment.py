readfile = open('input7_09_1.txt', 'r', encoding='utf-8')
words = {}
words_sorted = []
for line in readfile:
    for word in line.split():
        words[word] = words.get(word, 0) + 1
for key, item in words.items():
    words_sorted.append((-item, key))
for key, item in sorted(words_sorted):
    print(item)
