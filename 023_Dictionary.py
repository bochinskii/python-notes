
# Словарь (Dictionary)
# Это списки, элементы, которых имеют "ключ:значение"
print('*' * 30)
print('Словарь (Dictionary)')
print('*' * 30)

# Вариант определения словаря
print('- Вариант определения словаря')
product1 = {
    'Title': 'Sony',
    'Price': 100,
}
print(type(product1), product1)

# Еще один вариант определения словаря
print('- Еще один вариант определения словаря')
product1 = dict(
    Title='Iphone',
    Price=110
)
print(product1)

print()
# Преобразование списка в словарь
print('- Преобразование списка в словарь')

users = [
    ['Bob', 'bob@gmail.com'],
    ['Kate', 'kate@gmail.com'],
    ['Jhon', 'jhon@gmail.com'],
]
print(users, type(users))

d_users = dict(users)
print(d_users, type(d_users))


# Преобразование списка в словарь. При этом, элементы списка будут - ключами
print('- Преобразование списка в словарь. При этом, элементы списка будут - ключами')
print(dict.fromkeys(['price1', 'price2', 'price3']))

print()
# Сгенерировать словарь из последовательности чисел
print('- Сгенерировать словарь из последовательности чисел')
nums = {i: i + 1 for i in range(0, 11)}
print(nums)
print(nums[1])


print()
# Вывести значение определенного ключа
print('- Вывести значение определенного ключа')

product1 = {
    'Title': 'Sony',
    'Price': 100,
}
print(product1)

print(product1['Title'])
print('или')
print(product1.get('Title'))

print()
# Добавить в словарь ключ со значением
print('- Добавить в словарь ключ со значением')
product1['Designed'] = 'Japan'
print('или')
product1.update({'Store': 'Sony Corp.'})

print(product1)

# Удалить из словаря
del product1['Designed']
print('- Удалить из словаря')
print(product1)

print()
# Перебор словаря с помощью цикла. Выводится, только ключа
print('- Перебор словаря с помощью цикла. Выводится, только название ключа')
for key in product1:
    print(key)

# Перебор словаря с помощью цикла. Выводится, значение ключа
print('- Перебор словаря с помощью цикла. Выводится, значение ключа')
for key in product1:
    print(product1[key])

# Перебор словаря с помощью цикла. Выводится, ключ и значение
print('- Перебор словаря с помощью цикла. Выводится, ключ и значение')
for key, val in product1.items():
    print(f'{key}: {val}')


# Перебор списка, в котором есть словари с помощью цикла.
print('- Перебор списка, в котором есть словари с помощью цикла.')
products = [
    {'Title': 'Sony', 'Price': 20000},
    {'Title': 'Samsung', 'Price': 21000},
    {'Title': 'iPhone', 'Price': 80000},
    {'Title': 'Siemens', 'Price': 10000},
]

for i in products:
    print(f'{i.get("Title")}: {i.get("Price")}')

