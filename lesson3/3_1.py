def personal_data(a,b):
    c = a/b
    print(f'Результат деления: {c}')
    return

reply = input('Для начала работы алгоритма Type start: ')
while reply == 'y' or reply == 'start':
    try:
        a = int(input("Числитель: "))
        b = int(input("Делитель: "))
        try:
            personal_data(a,b)
        except ZeroDivisionError:
            print('Деление на 0 проивозаконно, пока отделаешься штрафом..Исправься!')
    except Exception:
            print("Аккуратнее с вводом, только цифры нужны")

    reply = input('Повторить? y/n: ')
print("До следующих встреч!)")

