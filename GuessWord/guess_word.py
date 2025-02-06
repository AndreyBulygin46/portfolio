"""
Игра угадай слово. Программа загазывает слово из набора слов в тектовом файле, а пользователь пытается у
гадать

"""
from random import choice

with open('WordForGame.txt', 'r', encoding='utf-8') as file:
    data = file.read().splitlines()

data = set(data)
list_answer = []


def new_game(data):
    words_for_game = []

    min_word = len(min(data, key=len))
    max_word = len(max(data, key=len))
    print('До скольки букв должно быть в слове?')
    number = int(input(f'Введите число от {min_word} до {max_word}: '))
    for word in data:
        if len(word) <= number:
            words_for_game.append(word)

    hidden_word = choice(words_for_game)
    hidden_word_mask = len(hidden_word) * '*'
    attempt = -1
    launch_game = False
    while True:
        attempts = input(
            'Введите количество попыток от 1 до 15 или наберите вых/ecs для выхода: ')
        print()
        if attempts == 'вых' or attempts == 'esc':
            print('До свидания!')
            launch_game = False
            break
        else:
            try:
                int(attempts)
            except ValueError:
                print('Введите число, пожалуйста!')
                continue
            else:
                if 1 <= int(attempts) <= 15:
                    attempts = int(attempts)
                    launch_game = True
                    break
                else:
                    print('Наберите число между 1 и 15!')
                    continue
    return hidden_word, hidden_word_mask, attempt, attempts, launch_game


hidden_word, hidden_word_mask, attempt, attempts, launch_game = new_game(data)


def questions():
    question = input('Сыграем ещё раз? д/н(да/нет): ')
    if question == 'д':
        question = True
    elif question == 'н':
        question = False
    return bool(question)


while launch_game:
    attempt += 1
    index = -1
    guessed_letters = 0
    if attempt < attempts:
        print('Для выхода наберите вых или ecs.')
        print(f'Осталось попыток: {attempts - attempt}\n')
    else:
        print('Закончились попытки.')
        print(f'Было загадно слово: {hidden_word}')
        question = questions()
        if question == True:
            hidden_word, hidden_word_mask, attempt, attempts, launch_game = new_game(
                data)
            question = False
        elif question == False:
            print('Спасибо за игру. До встречи!')
            break

    print(f'Загадано слово {hidden_word_mask} из {len(hidden_word)} букв.')
    answer = input('Введите букву или целое слово: ')

    if answer == 'вых' or answer == 'esc':
        print('До встречи!')
        break

    if answer == hidden_word:
        print(f'\nВерно, это слово {hidden_word}. Поздравляю!\n')
        question = questions()
        if question == True:
            hidden_word, hidden_word_mask, attempt, attempts, launch_game = new_game(
                data)
            question = False
        elif question == False:
            print('Спасибо за игру. До встречи!')
            break

    elif len(answer) > 1 and answer != hidden_word:
        print('\nНеверно. Попробуйте ещё раз!\n')

    if len(answer) == 1:
        for letter in hidden_word:
            index += 1
            if answer == letter:
                hidden_word_mask = hidden_word_mask[:index] + \
                    answer + hidden_word_mask[index+1:]
                guessed_letters += 1

    if guessed_letters > 0 and attempt != -1:
        print(f'\nУгадано букв: {guessed_letters}. Так держать!\n')

    elif guessed_letters == 0 and attempt != -1:
        print('\nНе угадали ни одной буквы. Попробуйте ещё!\n')

    list_answer += answer
    print(f'Вышли буквы: {list_answer}\n')
