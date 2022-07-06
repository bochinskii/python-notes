"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный).
Определите, есть ли в списке число, которое является индексом элемента "odd".
Напишите функцию, которая будет возвращать True или False, соответсвенно.
"""

print('*' * 10)
print('First task')
print('*' * 10)

# True
l1_t = ["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]
# False
l2_t = ["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]
# True
l3_t = ["even", 10, "odd", 2, "even"]


# Code for first task


get_bool = False
for i in l3_t:
    if i == 'odd':
        n = l3_t.index(i)
        for j in l3_t:
            if j == n:
                get_bool = True
                break
        break
print(get_bool)


# Function for first task
def odd_ball(arr):
    get_bool = False
    for i in arr:
        if i == 'odd':
            n = arr.index(i)
            for j in arr:
                if j == n:
                    get_bool = True
                    break
            break
    return get_bool


print(odd_ball(["even", 10, "odd", 2, "even"]))


"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно. 
Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. 
Попробуйте решить задачу двумя способами (один из способов в одну строчку кода).

find_sum(5) # return 8 (3 + 5)
find_sum(10) # return 33 (3 + 5 + 6 + 9 + 10)
"""
print('')
print('*' * 10)
print('Second tak')
print('*' * 10)


# Code v1 for second task
n1 = 5
n2 = 10

s = 0
for i in range(1, n1 + 1):
    a = i % 3
    b = i % 5
    if a == 0 or b == 0:
        s += i
print(s)

# Code v2 for second task
print(sum(i for i in range(1, n2 + 1) if i % 3 == 0 or i % 5 == 0))


# Function v1 for second task


def find_sum1(n):
    s = 0
    for i in range(1, n + 1):
        a = i % 3
        b = i % 5
        if a == 0 or b == 0:
            s += i
    return s


print(find_sum1(5))


# Function v2 for second task

def find_sum2(n):
    return sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0)


print(find_sum2(10))


"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""

print('')
print('*' * 10)
print('Third task')
print('*' * 10)


# Code for third task

names1 = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]


for i in names1:
    if len(i) != 4:
        names1.remove(i)
print(names1)


# Function for third task

def get_names(names):
    for i in names:
        if len(i) != 4:
            names.remove(i)
    return names


print(get_names(["Ryan", "Kieran", "Mark", "John", "David", "Paul"]))
