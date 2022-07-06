# Modules
print('*' * 30)
print('Встроенные модули')
print('*' * 30)

# Модуль - os
print('- Модуль - os')

import os

print(os.name)
print(os.getcwd())
print(os.getlogin())

# Выполнить системную комманду - dir
print('- Выполним системную комманду')
cmd = 'dir'
os.system(cmd)

# Создать диреткорию
os.mkdir('./my_dir', )

# Модуль - math
print('- Модуль - math')

import math as mm

print(mm.cos(1))

# Модуль - random (shuffle - перемешивает список, randint - возвращает случайное целое число)
print('- Модуль - random (shuffle - перемешивает список, randint - возвращает случайное целое число)')

from random import randint, shuffle

l = [1, 2, 3, 4, 5]
shuffle(l)
print(l)
print(randint(1, 10))

# Модуль - libs (get_count - считает количество определенных символов, get_len - считает длину слова)
print('- Модуль - libs (get_count - считает количество определенных символов, get_len - считает длину слова)')

import libs

print(libs.get_count('l', 'Hello'))
print(libs.get_len('Worlds'))



# Собственные модули
print('*' * 30)
print('Собственные модули')
print('*' * 30)

print('- перенесем раннее созданные функции в файл - my_own_modules. Теперь можно вызывать данные функции из файла')

import my_own_modules

my_own_modules.hello()

my_own_modules.performance('Denys', 25)

x = 10
y = 20
my_own_modules.suma_1(x, y)

print(my_own_modules.suma_2(55, 5))

print(my_own_modules.factorial(5))

print(my_own_modules.factorial_v2(5))

for i in range(1, 10 + 1):
   print(f'!{i} = {my_own_modules.factorial(i)}')

denis = my_own_modules.employeers('Denis', 25, '555-55-55', 'devops')
olya = my_own_modules.employeers('Olya', 24, '555-55-55', 'ingeneer')

l1 = list()
my_own_modules.reward(l1, 'Employer of mounth', 'Denis', 'Olya', 'Nikita', 'Zlata')
print(l1)

print('- Еще один вариант импорта модуля')

from my_own_modules import *

hello()
performance('Denys', 25)