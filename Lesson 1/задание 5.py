revenue = int(input('Your revenue: '))
costs = int(input('Your costs: '))
margin = revenue-costs
if revenue > costs:
    print('так держать, масштабируйся!')
    ror = (margin)/revenue*100
    print(f'{ror}%')
    employees = int(input('Your employees amount: '))
    print("Удельная прибыль на сотрудника: " + str((margin) / employees))
else:
    print('ты лузер, срочно покупай курсы "Бизнес молодость"')


