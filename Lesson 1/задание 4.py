# n = input("Go, pal, type number: ")
# result = list(n)
# i = 0
# maximum = 0
# while i < len(result):
#     if int(result[i]) > maximum:
#         maximum = int(result[i])
#     i += 1
# print(maximum)

# for result[i] in result:
#     if int(result[i]) > maximum:
#         maximum = int(result[i])
#     i += 1
# print(maximum)

"Решение с делением на 10"
n = int(input("Go, pal, type number: "))
maximum = 0
while n > 0:
    el = n % 10
    if el > maximum:
        maximum = el
    elif el == 9:
        break
    n = n//10
print(maximum)


