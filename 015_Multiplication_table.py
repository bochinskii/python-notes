# Таблица умножения (первый мой код на Python)

print('-' * 138)
print('Таблица умножения (грубый вариант с "while"):')
print('-' * 138)
i = 1
while i <= 9:
    print(f'1 x {i} = {1 * i}',
          f'\t2 x {i} = {2 * i}',
          f'\t3 x {i} = {3 * i}',
          f'\t4 x {i} = {4 * i}',
          f'\t5 x {i} = {5 * i}',
          f'\t6 x {i} = {6 * i}',
          f'\t7 x {i} = {7 * i}',
          f'\t8 x {i} = {8 * i}',
          f'\t9 x {i} = {9 * i}',
          sep='\t')
    i += 1
print('-' * 138)
print('-' * 138)

print('-' * 138)
print('Таблица умножения (грубый вариант с "for"):')
print('-' * 138)
for i in range(1, 9):
    print(f'1 x {i} = {1 * i}',
          f'\t2 x {i} = {2 * i}',
          f'\t3 x {i} = {3 * i}',
          f'\t4 x {i} = {4 * i}',
          f'\t5 x {i} = {5 * i}',
          f'\t6 x {i} = {6 * i}',
          f'\t7 x {i} = {7 * i}',
          f'\t8 x {i} = {8 * i}',
          f'\t9 x {i} = {9 * i}',
          sep='\t')
print('-' * 138)
print('-' * 138)

print('-' * 138)
print('Таблица умножения (наилучший вариант с "for"):')
print('-' * 138)
for i in range(1, 9 + 1):
    for j in range(1, 9 + 1):
        print(f'{j} x {i} = {j * i}', end='\t\t')
    print('')
