my_lst = [el for el in range(20,241) if el % 20 == 0 or el % 21 == 0]
print(my_lst)

def lst_if_gen(a,b):
    my_lst = [el for el in range(a,b+1) if el % 2 == 0]
    return my_lst