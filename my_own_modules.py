
def hello():
    '''Hello World function'''
    print('Hello')


def performance(name, age):
    '''Performance. Enter your name and age'''
    print(f'Hello, my name is {name}. I\'am {age} years old.')


def suma_1(f, s):
    '''Sum evaluation'''
    sum = f + s
    print(sum)


def suma_2(f, s):
    '''Sum evaluation and return a result'''
    sum = f +s
    return sum

def factorial(digit):
    '''Factorial evaluation'''
    factor = 1
    while digit > 1:
        factor = factor * digit
        digit = digit - 1
    return factor


def factorial_v2(digit):
    '''Factorial evaluation'''
    factor = 1
    for i in range(1, digit + 1):
        factor = factor * i
    return(factor)


def employeers(name, age, tel, position):
    emp = {
        'name': name,
        'age': age,
        'tel': tel,
        'position': position
    }
    return emp


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





















