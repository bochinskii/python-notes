"""
1. Дан список. Получите новый список, в котором каждое значение будет удвоено:
[1, 2, 3] --> [2, 4, 6]
"""

"""
2. Дан список. Возведите в квадрат каждый из его элементов и получит сумму всех полученных квадратов:
[1, 2, 3] --> 14 --> 1^2 + 2^2 + 3^2 = 14
"""

"""
3. Игорь любит кататься на велосипеде. Он знает, что при этом важно не допустить обезвоживания и пьет 0,5 литра воды в час. 
Вам дается время в часах, и вам нужно вернуть количество литров, которые Игорь выпьет, с округлением до наименьшего значения.
time1 = 3 --> litres = 1
time2 = 6.7 --> litres = 3
time3 = 11.8 --> litres = 5
"""

"""
4. Дана строка 'Hello world'. Проверьте, если в этой строке есть символ пробела - " ", тогда преобразуйте строку к верхнему регистру,
если же нет, тогда к нижнему.
***************
s = 'Hello world'
if stm:
	pass
else:
	pass
"""
# 1
print('-' * 15)
print('First')
print('-' * 15)

double_lst = [i * 2 for i in [1, 2, 3]]
print(double_lst)

double_lst2 = []
for i in range(1, 3 + 1):
    double_lst2.append(i * 2)
print(double_lst2)

# 2
print('-' * 15)
print('Second')
print('-' * 15)

squire_lst = [i ** 2 for i in [1, 2, 3]]
print(squire_lst, f'Сумма элементов списка равна {squire_lst[0] + squire_lst[1] + squire_lst[2]}')

squire_lst2 = []
for i in range(1, 3 + 1):
    squire_lst2.append(i ** 2)
print(squire_lst2, f'Сумма элементов списка равна {squire_lst2[0] + squire_lst2[1] + squire_lst2[2]}')

# 3
print('-' * 15)
print('Tirth')
print('-' * 15)

print(f'time1 = 3 --> litres = {int(0.5 * 3)}')
print(f'time1 = 6.7 --> litres = {int(0.5 * 6.7)}')
print(f'time1 = 11.8 --> litres = {int(0.5 * 11.8)}', end='\n\n')

import math

print(f'time1 = 3 --> litres = {math.floor(0.5 * 3)}')
print(f'time1 = 6.7 --> litres = {math.floor(0.5 * 6.7)}')
print(f'time1 = 11.8 --> litres = {math.floor(0.5 * 11.8)}')

# 4
print('-' * 15)
print('Fourth')
print('-' * 15)

s = 'Hello World'
for i in s:
    if i == ' ':
        sig = 1
        break
else:
    sig = 0

if sig > 0:
    print(s.upper())
else:
    print(s.lower())
