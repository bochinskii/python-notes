
name = 'Denys'
age = 34

# Используем форматирование строки
print('*' * 30)
print('Используем форматирование строки')
print('*' * 30)

# Не очень хорошие варианты (можно запутаться)
print('- Не очень хорошие варианты (можно запутаться)')
print('My name is ' + name + '. ' + 'I\'am ' + str(age) + ' years old.')
print('My name is %(n)s. I\'am %(a)d years old.' %{'n': name, 'a': age})
print('My name is %s. I\'am %d years old.' %(name, age))

# Еще одни не очень хорошие варианты (можно запутаться)
print('\n')
print('- Еще одни не очень хорошие варианты (можно запутаться)')
print('My name is {}. I\'am {} years old.'.format(name, age))
print('My name is {0}. I\'am {1} years old.'.format(name, age))
print('My name is {0}. I\'am {1} years old. So i live {1} years on this Earth.'.format(name, age))
print('My name is {n}. I\'am {a} years old. So i live {a} years on this Earth.'.format(n=name, a=age))

# А этот вариант очень расспространенный и используется часто
print('\n')
print('- А этот вариант очень расспространенный и используется часто')
print(f'My name is {name}. I\'am {age} years old. So I live {age} years on this Earth.')
print(f'My name is {name}. I\'am {age} years old. So I think that will live {age + 50} years on this Earth.')
