from itertools import cycle, count

def a_count(a,h,st):

    count_lst = []
    for el in count(a, h):
        if el > st:
            break
        else:
            count_lst.append(el)
    return count_lst

def b_cycle(n):
    cycle_lst = []
    i = 0
    for el in cycle('1234'):

        if i >= n:
            break
        else:
            cycle_lst.append(el)
            i += 1
    return cycle_lst

def true_while():
    if input("Повторить? (Y/N) При отказе начнем решать вторую задачу.") == 'N':
        return False
    else:
        return True


i = 0
reply = input("Задача состоит из двух частей. Какую запустить первой? \n   а). итератор, генерирующий целые числа, начиная с указанного\n   б). итератор, повторяющий элементы некоторого списка, определенного заранее\n Твой выбор: ")
while i < 2:
    if reply == 'а':
        my_intent = True
        i += 1
        while my_intent == True:
            reply = 'б'
            inp_str = input("Начальное значение и шаг и ограничение через пробел: ")
            inp_lst = inp_str.split()
            a = int(inp_lst[0])
            h = int(inp_lst[1])
            st = int(inp_lst[2])
            print(a_count(a, h, st))
            my_intent = true_while()

    else:
        my_intent = True
        i += 1
        while my_intent == True:
            reply = 'а'
            n = int(input("Сколько элементов вывеси? Ответ: "))
            print(b_cycle(n))
            my_intent = true_while()
