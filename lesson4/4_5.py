# from /Users/georgijmalkov/Documents/Geekbrains/Основы языка Python /Lesson 4/4_3.py import lst_if_gen
# import 4_3 "Почему мой модуль не импортируется, чтобы из задании 4_3 сразу взять нужную функцию"
from functools import reduce

def lst_if_gen(a,b):
    my_lst = [el for el in range(a,b+1) if el % 2 == 0]
    return my_lst

print(f'Множество всех четных цисел в заданном промежутке значений вашего списка: {reduce(lambda x,y: x*y, lst_if_gen(1,5))}')