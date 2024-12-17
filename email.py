'''Будем считать адрес email корректным, если в нём есть символ @ и точки.
При этом отсутствуют пробелы. Напишите программу, которая будет проверять корректность адреса email.

На вход программе подаётся строка – адрес email.
Программа должна вывести булево значение True,
если адрес email является корректным и False – в случае некорректного ввода адреса email.

Пример 1
Пример входных данных:
helloworld@mail.ru

Пример ответа:
True

Пример 2
Пример входных данных:
Hello world@ ya.ru

Пример ответа:
False'''

def check_email(email: str) -> bool:
    if '.' in email and '@' in email and ' ' not in email:
        return True
    else:
        return False

if __name__ == '__main__':
    assert check_email('Helloworld@.ru') is True
    assert check_email('мояпочта@нетология.ру') is True
    assert check_email('python@email@net') is False
    assert check_email(' em@il.ru') is False
    print("\nОтличная работа, отправляйте на проверку!")

