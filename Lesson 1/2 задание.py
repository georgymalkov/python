num = input("Введи твое значение: ")
hour = 0
minute = 0
sec = 0
while num.isdigit() == False:
    num = input('Ошибочка, у тебя жирные пальцы, давай еще разок:')

hour = int(num) // 3600
minute = int(num) % 3600 // 60
sec = (int(num) % 3600) % 60
print(hour, ':', minute, ':', sec)

# Приведение результатов к формату 00:00:00, как это сделать проще?
if hour < 10 and minute < 10 and sec < 10:
    print('0'+str(hour)+':0'+str(minute)+':0'+str(sec))
elif minute < 10 and sec < 10:
    print(str(hour)+':0'+str(minute)+':0'+str(sec))
elif sec < 10:
    print(str(hour)+':'+str(minute)+':0'+str(sec))
elif hour < 10 and sec < 10:
    print('0'+str(hour)+':'+str(minute)+':0'+str(sec))
elif hour < 10 and minute < 10:
    print('0' + str(hour) + ':0' + str(minute) + ':' + str(sec))

"Через f - строку"
print(f'{hour:02d}:{minute:02d}:{sec:02d}')
