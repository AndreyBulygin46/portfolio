'''На вход программе подаётся строка. 
Напишите программу, которая вернёт строку, переписанную в обратном порядке строчными символами.

Пример входных данных:
QwertY

Пример ответа:
ytrewq'''

def reverse(string: str) -> str:
    # Напишите ваш код здесь
    return string[::-1].lower()


if __name__ == '__main__':
    assert reverse('!dlroW olleH') == 'hello world!'
    assert reverse('AvadaKedavraaaaA!') == '!aaaaarvadekadava'
    assert reverse('хаЗерс хишав ХИТЭ в ясларбозар от-ценокан Я') == 'я наконец-то разобрался в этих ваших срезах'
    print("\nОтличная работа, отправляйте на проверку!")
