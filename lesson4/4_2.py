import random

def list_gen(n):
    lst = []
    for el in range(0,n):
        lst.append(round(random.random()*200, 2))
    return lst

def new_list_gen(n):
    new_lst = []
    lst = list_gen(n)
    print(lst)
    for i in range(0,len(lst)-1):
        if lst[i]<lst[i+1]: new_lst.append(lst[i])
    return new_lst

try:
    print(new_list_gen(int(input("Количество символов в списке: "))))
except Exception:
    print('Лажа')

# print(list_gen(int(input("Количество символов в списке: "))))

