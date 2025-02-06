"""Напишите программу, которая проверяет логин (переменная login)и пароль (переменная password) пользователя. 
Если логин равен “admin” и пароль равен “password”, выведите сообщение «Добро пожаловать», иначе выведите сообщение «Доступ ограничен».

В этом задании корректность работы кода проверяется тестом.
Для работы теста необходимо написать код функции. Обращайте внимание на подсказки к заданиям и комментарии в шаблоне кода.

Более подробно с синтаксисом функции вы сможете познакомиться на последующих занятиях."""



def check_auth(login: str, password: str):

    if login == 'admin' and password == 'password':
        result = 'Добро пожаловать'
    else:
        result = 'Доступ ограничен'
    return result


if __name__ == '__main__':
    auth = check_auth('user', 'password')
    assert auth == 'Доступ ограничен', f'Получен неверный ответ: {auth}'
    print('Неверный login:', auth)

    auth = check_auth('admin', '123')
    assert auth == 'Доступ ограничен', f'Получен неверный ответ: {auth}'
    print('Неверный password:', auth)

    auth = check_auth('admin', 'password')
    assert auth == 'Добро пожаловать', f'Получен неверный ответ: {auth}'
    print('Верные login, password:', auth)
