string = input('Твоя строка, нескольок слов через " ", если не слабо: ')
lst = string.split(' ')
print(lst)
print(len(lst))
# for ind, el in enumerate(lst):
#     print(ind, el[0:10])

"Альтернативное решение через Словарь"
per = {}
i = 1
for el in lst:
    per[i] = el
    i = i + 1
for key, value in per.items():
    print(f"{key} - {value[1:10]}")



