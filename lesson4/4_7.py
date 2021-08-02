from itertools import count
from functools import reduce

def fact(n):
    for i in count(1):
        if i <= n:
            result = reduce(lambda x,y: x*y, range(1,i+1))
            yield result
        else:
            break

n = int(input("Ваше число: "))
res_lst=[]
for el in fact(n):
    res_lst.append(el)
print(res_lst)