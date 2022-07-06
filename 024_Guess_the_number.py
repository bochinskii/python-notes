'''
Создайте игру "Угадай число". В коде программы в переменную запишите любое число от 1 до 100
(в следующих уроках мы узнаем, как генерировать случайное число), которое и должен угадать игрок.
Далее программа должна спросить у игрока угадать число. Если пользователь не угадал число - программа сообщает,
что загаданное число больше/меньше и предлагает попробовать еще раз, при этом программа ведет счета кол-ва попыток игрока.
Если игрок угадал число, тогда программа благодарит за игру и сообщает кол-во попыток, за которое было угадано число.
'''
print('*' * 50)
print('Угадай число'.center(50))
print('*' * 50)

import os
import random

number = random.randint(1, 100)
gamer_number = 0
tries = 5
tries_number = 0
agreement = input('Добро пожалова в игру "Угадай число". \n\
Если хотите начать играть нажмите - "y". Если хотите выйти, нажмите "n": ')
if agreement != 'y':
    exit()
while gamer_number != number and tries > 0 or gamer_number == 0:
    if tries == 5:
        suf1 = 'ок'
    if 1 < tries < 5:
        suf1 = 'ки'
    if tries == 1:
        suf1 = 'ка'
    gamer_number = int(input(f'Введите число от 1 до 100 и выграйте приз - удар по ебальцу :). \
У вас на это есть {tries} попыт{suf1}. Поехали - '))
    print('*' * 50)
    tries -= 1
    tries_number += 1
    if tries == 5:
        suf1 = 'ок'
        suf0 = 'ось'
    if 1 < tries < 5:
        suf1 = 'ки'
        suf0 = 'ось'
    if tries == 1:
        suf1 = 'ка'
        suf0 = 'ась'
    if tries_number == 5:
        suf3 = 'ок'
    if 1 < tries_number < 5:
        suf3 = 'ки'
    if tries_number == 1:
        suf3 = 'ку'
    if gamer_number < number and tries > 0:
        print('*' * 50)
        print(f'Ваше число - "{gamer_number}" меньше загаданного. Попробуйте еще раз. \
Вы же хотите получить отменных пиздюлей? У вас остал{suf0} {tries} попыт{suf1}')
        print('*' * 50)
    elif gamer_number > number and tries > 0:
        print(f'Ваше чилсо - "{gamer_number}" больше загаданного. Попробуйте еще раз. \
Вы же хотите получить отменных пиздюлей? У вас остал{suf0} {tries} попыт{suf1}')
        print('*' * 50)
    elif gamer_number == number and tries >= 0:
        print(f'Вы УГАДАЛИ!!!! Ваше введенное число - "{gamer_number}" совпало с загаданным числом - "{number}". \
Вы проделали - "{tries_number}" попыт{suf3}. Можите приходить за пиздюлями.')
    else:
        print('*' * 50)
        agreement2 = input(f'Вы проиграли (исчерпали 5 попыток). Загаданное число было - {number}\n \
Печалька :(. Придется Вам получиать пиздюлей в другом месте.\n \
Нажмите - "y", если хотите попробовать еще раз или - "n", если хотите выйти: ')
        print('*' * 50)
        if agreement2 != 'y':
            exit()
        else:
            gamer_number = 0
            tries = 5
            tries_number = 0
            number = random.randint(1, 100)
            os.system('cls' if os.name == 'nt' else 'clear')
