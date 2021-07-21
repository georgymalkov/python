# print(a = input('Введи число:'))
# Почему данное выражение ошибкой отображается?

a = input('Введи число:')
while a.isdigit() == False:
    a = input('Что за кракозябра, давай мне число:')
print(a)
b = input ('Напиши что-нибудь:')
c= input ('write more:')
print(b+' '+c)
print(f'{b} {c}')
