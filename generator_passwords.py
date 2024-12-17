""" 
генератор паролей. Должен работать так, чтобы пользователь мог задать длину пароля.

"""
from random import choice


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = alphabet.upper()
numbers = '123456798'

password_length = int(input('Введите длину пароля: '))
password = ''

while True:
    for _ in range(password_length):
        alphabet_cho       = choice(alphabet)
        alphabet_upper_cho = choice(alphabet_upper)
        numbers_cho        = choice(numbers)
        password_intermediate = alphabet_cho + alphabet_upper_cho + numbers_cho
        password_intermediate_cho = choice(password_intermediate)
        password += password_intermediate_cho

    print(f'Ваш пароль: {password}')
    question = input('Нажмите enter, чтобы передалать пароль или наберитe вых для выхода/esc: ')
    if question == 'вых' or question == 'esc':
        print('До встречи!')
        break
    else:
        password = ''
        continue
