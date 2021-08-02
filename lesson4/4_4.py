def unique_var(lst):
    unique_lst = [el for el in lst if lst.count(el) == 1]
    return unique_lst

lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
try:
    print(f'Исходный список: {lst} \nСформированный список: {unique_var(lst)}')
except Exception:
    print('Ошибка 404')

if __name__ != '4_4':
    pass