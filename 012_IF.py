# Используем сравнение IF
print('*' * 30)
print('Используем сравнение IF')
print('*' * 30)

# Есть вот такие условия, которые возвращяют булевое значение
print('- Есть вот такие условия, которые возвращяют булевое значение')
print(2 > 3)
print(2 < 3)

# 1-й пример. Если использовать IF без условия, то оно вернет - true, если число не равно нулю
print('- 1-й пример. Если использовать IF без условия, то оно вернет - true, если число не равно нулю')

x = 0
if x:
    print('Переменная x не равна нулю')
else:
    print('Переменная x равна нулю')

y = -1
if y:
    print('Переменная y не равна нулю')
else:
    print('Переменная y равна нулю')


# 2-й пример. Сравнение строк.
print('- 2-й пример. Сравнение строк.')

light = 'red'
if light == 'red':
    print('Do not walk')
elif light == 'yellow':
    print('Do not walk, but redy')
else:
    print('Walk')

# 3-й пример. Сравнение чисел и ввод пользовательских данных.
print('- 3-й пример. Сравнение чисел и ввод пользовательских данных.')

age = int(input('How old are You?: '))
if age <= 17:
    print('You can not fucking and drink a vodka!!!!')
    print(f'You {age} years old. You have {18 - age} years that you can fucking and {21 - age} for drinking vodka')
elif age < 21:
    print('You can not drink a vodka!!!!')
    print(f'You {age} years old. You have {21 - age} that you can drink a vodka')
else:
    print('Congratulation. You can fucking and drink a vodka :)')

# 4-й пример. Использование логических операторов.
print('- 4-й пример. Использование логических операторов.')

time = 5
day = 'Mon'
if time > 7 and day != 'St' and day != 'Sun':
    print('Welcome')
else:
    print('Sorry. We are not working!')

# 5-й пример. Короткая форма записи - IF
print('- 5-й пример. Короткая форма записи - IF')
x = 0
res = 'Ok' if x > 0 else 'NOT OK'
print(res)

