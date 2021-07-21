a = int(input("Начинал бегать по, км: "))
b = int(input("Цель, км: "))
i = 1
zametki = dict()
zametki[str(i) + '-й день'] = a
while a < b:
    a = a + a*0.1
    i = i+1
    zametki[str(i) + '-й день'] = a
print(i)
print(zametki) #Почему после 3 дня, значения сохраняются неверные (много знаков после запяттой)? Как это исправить?
