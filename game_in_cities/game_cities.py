from random import choice


list_of_cities_small = []
excluded_cities = set()
switch_for_game = False
start_game = True
continue_game = False
question = input('Готовы сыграть? (да/нет): ')

with open('citiesForGame.txt', 'r', encoding='utf-8') as file:
    data = set(file.read().splitlines())

for word in data:
    word_small = word.lower()
    list_of_cities_small.append(word_small)


if question == 'да':
    print('Начинаем игру.\n')
    switch_for_game = True

elif question == 'нет':
    print('Хорошо. До встречи!')
    switch_for_game = False


while switch_for_game:
    list_of_cities = set(list_of_cities_small)
    list_for_game = list_of_cities.difference(excluded_cities)
    list_for_random = set()
    count = 0

    print('Для выхода наберите вых или esc!')
    print(f'Вышли города: {excluded_cities}')

    if start_game:
        mysterious_city = choice(list(list_for_game))
        excluded_cities.add(mysterious_city)
        start_game = False
    else:
        for citi in list_for_game:
            if letter == citi[0]:
                list_for_random.add(citi)
        continue_game = True

    if len(list_for_random) == 0 and continue_game:
        print('Вы выиграли. Поздравляю!!!')
        break
    elif len(list_for_random) > 0 and continue_game:
        mysterious_city = choice(list(list_for_random))
        excluded_cities.add(mysterious_city)

    if mysterious_city[-1] == 'ь' or mysterious_city[-1] == 'ъ':
        letter = mysterious_city[-1-1]
        print(f'Выбран город: "{mysterious_city}", вам на "{mysterious_city[-1-1]}"')
    else:
        letter = mysterious_city[-1]
        print(f'Выбран город: "{mysterious_city}", вам на "{mysterious_city[-1]}"')

    answer = input(f'Введите город на "{letter}": ')

    if answer == 'вых' or answer == 'esc':
        print('Спасибо за игру. До встречи!')
        break

    for _ in range(3):
        count += 1

        if answer in list_for_game and answer[0] == letter:
            excluded_cities.add(answer)
            if answer[-1] == 'ь' or answer[-1] == 'ъ':
                letter = answer[-1-1]
                break
            else:
                letter = answer[-1]
                break
        else:
            print(f'"{answer}" не подходит.')
            print(f'Осталось попыток: {3 - count}')
            answer = input(f'Введите город на "{letter}": ')
            if count == 3 or answer == 'вых' or answer == 'esc':
                print('Спасибо за игру. До встречи!')
                switch_for_game = False
                break