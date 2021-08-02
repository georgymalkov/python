from sys import argv

script_name, time, bid, bonus = argv

print("Script: ", script_name)
print("Your Time: ", time)
print("Your bid: ", bid)
print("Your bonus: ", bonus)

try:
    my_salary = int(time) * int(bid) * ((float(bonus)/100)+1)
    print(my_salary)
except ValueError:
    print("Не достает введенных данных, проверь значения на входе!")

# import random
#
# def salary():
#     time = random.randint(0, 50)
#     bid = random.random() + 2
#     if time > 24:
#         my_salary = time * bid * 1.3
#         return my_salary, time, bid
#     else:
#         my_salary = time * bid
#         return my_salary, time, bid
#
#
# try:
#     print(f'Ваша зарплата: {salary()}')
# except Exception:
#     print("Неопознанная ситуевина")
#
# if __name__ != '4_1':
#     pass
