'''Условие задачи
Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек (их число может варьироваться):

1
2
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
Выдвигаем гипотезу: мы получим лучшие рекомендации,
если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки.

Обратите внимание, что если количество людей в списках будет не совпадать,
то мы никого не будем знакомить и выведем пользователю предупреждение, что кто-то может остаться без пары.

В этом задании корректность работы кода проверяется тестом. Для работы теста необходимо написать код функции.
Обращайте внимание на подсказки к заданиям и комментарии в шаблоне кода.

Более подробно с синтаксисом функции вы сможете познакомиться на последующих занятиях.'''

def solve(boys: list, girls: list):
    result = "" # в эту строку сохраните полученные пары или сообщение "Кто-то может остаться без пары!"
    boys.sort()
    girls.sort()
    if len(boys) == len(girls): # проверьте, что длины списков одинаковы
        for solves in zip(boys, girls): # отсортируйте пары, объедините при помощи zip и распакуйте в цикле
            result += f'{solves[0]} и {solves[1]}, '
        result = result[:-2]
    else:
        result = 'Кто-то может остаться без пары!'
    return result

if __name__ == '__main__':
    # Этот код менять не нужно
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = solve(boys, girls)
    assert result == "Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = solve(boys, girls)
    assert result == "Кто-то может остаться без пары!", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma']
    result = solve(boys, girls)
    assert result == "Кто-то может остаться без пары!", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")


