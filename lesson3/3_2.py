def personal_data(**kwargs):
    """
    Отображается введенные пользователем параметры: имя, фамилия, год рождения, город проживания, email, телефон
    :param kwargs: вводятся с клавиатуры
    :return: введенный результат
    """
    return kwargs

print(personal_data(name = input('Ваше Имя: '), surame = input('Ваша Фамилия: '), city = input('Город проживания: '), email = input('Ваш email: '), mob = input('Ваш мобильный номер: ')))