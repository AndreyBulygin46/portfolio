'''Условие задачи
Напишите программу, которая выведет все фразы из списка phrases, которые являются палиндромами:

1
2
3
4
5
6
7
8
9
10
phrases = [
           "нажал кабан на баклажан",
           "дом как комод",
           "рвал дед лавр",
           "азот калий и лактоза",
           "а собака боса",
           "тонет енот",
           "карман мрак",
           "пуст суп"
]
Палиндром – это фраза, которая читается одинаково в любую сторону. Самый известный палиндром: «А роза упала на лапу Азора».

В этом задании корректность работы кода проверяется тестом. Для работы теста необходимо написать код функции.
Обращайте внимание на подсказки к заданиям и комментарии в шаблоне кода.

Более подробно с синтаксисом функции вы сможете познакомиться на последующих занятиях.'''


def solve(phrases: list):
    result = [] # список палиндромов
    for phrase in phrases: # пройдите циклом по всем фразам
        clear_phrase = phrase.replace (' ', '') # сохраните фразу без пробелов
        if clear_phrase == clear_phrase[::-1]: # сравните фразу с ней же, развернутой наоборот (через [::-1])
            result.append(phrase)
    return result

if __name__ == '__main__':
    # Этот код менять не нужно
    phrases = ["нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "карман мрак", "пуст суп"]
    result = solve(phrases)
    assert result == ["нажал кабан на баклажан", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "пуст суп"], f"Неверный результат: {result}"
    print(f"Палиндромы: {result}")

