import random

def easy_pow(x,y):
    new_x1 = x**y
    # new_x2 = pow(x,y)
    return new_x1

def hard_pow(x,y):
    # length = abs(y)
    if y > 0:
        print("Читай внимательнее задание")
    elif y == 0:
        new_x2 = 1
        return new_x2
    else:
        for i in range(1, abs(y)): x *= x
        new_x2 = 1 / x
        return new_x2

print(f'Результаты первой функции:{easy_pow(random.randint(1,5),random.randint(-3,-1))}')
print(f'Результаты второй функции:{hard_pow(random.randint(1,5),random.randint(-3,-1))}')
if easy_pow(9,0) == hard_pow(9,0): print('Все работает, ура, ура, ура!')