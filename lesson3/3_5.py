def sum(my_str):
    lst = my_str.split()
    sum = 0
    for el in lst:
        try:
            try:
                if el == ' ' or float(el):
                    sum += float(el)
            except Exception:
                print('Ты видимо опечатался, добавил "не цифру", вот я и вылетел.')
                print('Если хочешь исправиться, напиши ниже "Reset"')
                print('Если опечатка не помешала вводу твоих значений*,то пиши "Go"')
                print('*(Опечатка после всех чисел и не пишется слитно с ними)')
                reply = input("Твой отве - ")
                if reply == "Reset":
                    sum = 0
                    return sum,True
                elif reply == "Go":
                    return sum, True
                return sum, False
        except ValueError:
            continue
    return sum, True

con_flag = True
result = 0
while con_flag:
    inp_str = input("Ведите ваши числа через пробел. Для остановки введи любой не числовой символ: ")
    res_sum, con_flag = sum(inp_str)
    result += res_sum

print(f'Вроде для машины посчитал верно: {result}')



# def sum(my_str):
#     lst = my_str.split()
#     sum = 0
#     for el in lst:
#         try:
#             if el == 'S' or el == 's' or el == 'Stop' or el == 'stop' or el == 'ытоз':
#                 return sum, False
#             else:
#                 sum += float(el)
#         except ValueError:
#             continue
#     return sum, True
#
# con_flag = True
# result = 0
# while con_flag:
#     inp_str = input("Ведите ваши числа через пробел. Для остановки ввода Type S aka Stop.Ваши числа: ")
#     res_sum, con_flag = sum(inp_str)
#     result += res_sum
#
# print(f'Вроде для машины посчитал верно: {result}')