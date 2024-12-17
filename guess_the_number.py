from random import randint as ran

cont_begin = 0

while True:
    ready = input("Готовы сыграть да/нет: ")
    if ready == "да":
        while True:
            if cont_begin == 0:
                try:
                    begin = int(input("Введите целое число начала диапазона: "))
                    cont_begin += 1
                except ValueError:
                    print("Нужно ввести целое число!")
                    continue
            elif cont_begin == 1:
                try:
                    ends = int(input("Введите целое число окончания диапазона: "))
                except:
                    print("Нужно ввести целое число!")
                    continue
                else:
                    break
        random_number = ran(begin, ends)
        print("Игра запущена!")
        print('Для выхода напишите "выход" в поле для ввода.')
        hint = None
        count = 0
        state = True
        break

    elif ready == "нет":
        print("Очень жаль. Будем ждать вашего возвращения!")
        hint = False
        state = False
        break
    else:
        print("Нужно ввести да или нет")
        continue

while hint == None and count == 0:
    question = input("Включить подсказки(да/нет): ")

    if question == "да":
        hiht = True
        count += 1
        break

    elif question == "нет":
        hiht = False
        count += 1
        break

    elif question == "выход":
        state = False
        print("Жаль, что уходите. До встречи!")
        break

    else:
        print('Введите "да" или "нет"')
        continue

while state:

    guessed_number = input(f"Введите целое число между {begin} и {ends}: ")

    if guessed_number == "выход":
        print("Спасибо за игру, до встречи!")
        break

    try:
        int(guessed_number)
        if begin > int(guessed_number) or int(guessed_number) > ends:
            print(f"Ошибка. Число {int(guessed_number)} не подходит по параметрам!")
            continue

        elif int(guessed_number) == random_number:
            print(f"Вы победили, это число {random_number}. До встречи!")
            break

        else:
            if hiht == True:
                (
                    print("Ваше число больше загаданного. Попробуйте ещё раз!")
                    if int(guessed_number) > random_number
                    else print("Ваше число меньше загаданного. Попробуйте ещё раз!")
                )
                continue
            else:
                print("Не угадали. Попробуйте ещё раз!")

    except ValueError:
        print("Ошибка! Строка не является целым числом!")
        continue
