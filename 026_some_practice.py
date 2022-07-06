#1
print('*' * 15)
print('1. Указать последовательность чисел и умножить их на определенное число')
print('*' * 15)


def double_f(first, last, factor):
    double = [i*factor for i in range(first, last)]
    print(double)


double_f(1, 4, 2)

#2
print('*' * 15)
print('2. Возведение в степень')
print('*' * 15)


def squire_f(first, last, stage):
    squire = []
    for i in range(first, last):
        squire.append(i ** stage)
    print(squire)


squire_f(1, 4, 2)