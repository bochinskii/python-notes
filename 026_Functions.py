# Functions
print('*' * 30)
print('Функции')
print('*' * 30)

# Определяем функцию без парамметров
def hello():
    '''Hello World function'''
    print('Hello')

# Вызываем функцию без парамметов
print('- Вызываем функцию без парамметров 3 раза')

hello()
hello()
hello()

# Определяем функцию с парамметрами
def performance(name, age):
    '''Performance. Enter your name and age'''
    print(f'Hello, my name is {name}. I\'am {age} years old.')

# Вызываем функцию с парамметрами
print('- Вызываем функцию с парамметрами 2 раза')

performance('Denys', 25)
performance('Olya', 24)


# Пример функции с числами
def suma(f, s):
    '''Sum evaluation'''
    sum = f + s
    print(sum)

# Вызываем функцию с числами
print('- Вызываем функцию с числами')
x = 65
y = 500
suma(x, y)

# Пример функции с возвращением результата (return)
def suma(f, s):
    '''Sum evaluation and return a result'''
    sum = f +s
    return sum

# Вызываем функцию с возвращением результата (return)
print('- Вызываем функцию с числами (return)')
print(suma(55, 5))


# Пример функции подсчитывающая факториал (использование while)
def factorial(digit):
    '''Factorial evaluation'''
    factor = 1
    while digit > 1:
        factor = factor * digit
        digit = digit - 1
    return factor

# Вызываем функцию подсчитывающая факториал (использование while)
print('- Вызываем функцию подсчитывающая факториал (использование while)')

print(factorial(5))

# Пример функции подсчитывающая факториал (использование for)
def factorial_v2(digit):
    '''Factorial evaluation'''
    factor = 1
    for i in range(1, digit + 1):
        factor = factor * i
    return(factor)

# Вызываем функцию подсчитывающая факториал (использование for)
print('- Вызываем функцию подсчитывающая факториал (использование for)')

print(factorial_v2(5))


# Вызываем функцию подсчитывающая факториал красивым образом
print('- Вызываем функцию подсчитывающая факториал красивым образом')

for i in range(1, 10 + 1):
   print(f'!{i} = {factorial(i)}')


# Функции, которые строят словари и списки
print('*' * 30)
print('Функции, которые строят словари и списки')
print('*' * 30)

# Пример функции, которая строит словарь
def employeers(name, age, tel, position):
    emp = {
        'name': name,
        'age': age,
        'tel': tel,
        'position': position
    }
    return emp

# Вызываем функцию, которая строит словарь
print('- Вызываем функцию, которая строит словарь')
denis = employeers('Denis', 25, '555-55-55', 'devops')
olya = employeers('Olya', 24, '555-55-55', 'ingeneer')

print(denis)
print(olya)


# Пример функции с неопределенным количеством парамметров, которая генерирует список со словарями
def reward(lst, rew, *names):
    '''
      Create dictionaries for reward and add it to list.
      Do not forget define a empty list
    '''
    for name in names:
        d = {
            'name': name,
            'rew': rew
        }
        lst.append(d)


# Вызываем функцию сс неопределенным количеством парамметров, которая генерирует список со словарями
print('- Вызываем функцию с неопределенным количеством парамметров, которая генерирует список со словарями')

l1 = list()
reward(l1, 'Employer of mounth', 'Denis', 'Olya', 'Nikita', 'Zlata')

print(l1)




















