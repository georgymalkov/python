n = input("Введи твое значение: ")

while n.isdigit() == False:
    n = input('ну ты даешь, давай еще разок:')

print(int(n)+int(n+n)+int(n+n+n))