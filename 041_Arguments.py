# аргументы
print('*' * 30)
print('Аргументы')
print('*' * 30)

import sys

# Првоерять нужно вот таким образом: python .\041_Arguments.py Denis 25
# где, Denis 25 - пример аргументов

# Выводит все арументы
print('- Выводит все арументы')

print(sys.argv)



# Вывести все аргументы, кроме 0-го т.к. 0-й агрумент - это имя файла. Как в bash - $0
print('- Вывести все аргументы, кроме 0-го т.к. 0-й агрумент - это имя файла')

print(sys.argv[1:])



# Вывести определенный агрумент. Как в bash - $1, $2 и т.д
print('- Вывести определенный агрумент')

# Закомментируйте, когда будете использовать аргументы ниже (иначе будет ошибка)
# print(sys.argv[1])


# Вывести количество аргументов, которое было передано. В bash - $#
# - 1 т.к. 0-й аргумент есть всегда (имя файла)
print('- Вывести количество аргументов, которое было передано')

print(len(sys.argv) - 1)


# Используем аргументы
print('- Используем аргументы')

if (len(sys.argv) - 1) == 0:
    print('Arguments are not provided')
    sys.exit()
elif (len(sys.argv) - 1) == 1 or sys.argv[1] == '/?':
    print('Enter two arguments: your name and your age')
    sys.exit()
else:
    print(f'Hello, my name is {sys.argv[1]}. I\' am {sys.argv[2]} years old')


