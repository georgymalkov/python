def up_text(text):
    """
    на входе принимаются слова любого формата
    :param text: ввод с клавиатуры, слово или строка из нескольких слов, разделенных пробелами
    :return: Делает первые буквы слов заглавными
    """
    while text.lower() == False:
        text = input ("Я не собираюсь это принимать, удостой меня текстом из маленьких букв! - ")
    # if text.islower() == False: print("Я конечно твой текст приму, но пиши все только с маленькой буквы в след. раз") "включить при отказе от цикла от неправильного ввода "
    new_text = text.title()
    return new_text

text = input("Давай свои буковки: ")
while text.islower() == False:
        text = input("Я не собираюсь это принимать, удостой меня текстом из маленьких букв! - ")
print(f'Я немного поработал с твоим текстом - {up_text(text)}')

func_2 = lambda text: text.title()
print(f'Я немного поработал с твоим текстом - {func_2}') "Почему ее не принт?"


"Пытался усложнить жизнь, но почему- о не работает..В чем дело?"
# def up_text(text):
    # print(text)
    # for el in text:
    #     el[0].upper()
    #     break
    # text.upper()
    # print(text)
    # if text.isdigit():
    #     return 'Глаза ON и пробуй еще раз'
    # else:
    #     text.lower()
    # return text



