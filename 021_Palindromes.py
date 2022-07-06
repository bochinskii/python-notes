words = ['мадам', 'топот', 'test', 'madam', 'words']
my_str = ['Oko za oko', 'А роза упала на лапу Азора', 'Около Миши молоко']

# In one string
print('-' * 50)
print('Первый, самый лучший метод')
print('-' * 50)

# Используем срез при сравнении слова
print([i for i in words if i == i[::-1]])

# Сперва удаляем пробелы, переводим в один из регистров и сравниваем с помощью среза
print([i for i in my_str if i.replace(' ', '').lower() == i[::-1].replace(' ', '').lower()])

print()
# Not one string
print('-' * 50)
print('Второй, метод по-хуже')
print('-' * 50)

for i in words:
    if i[::-1] != i[::1]:
        words.remove(i)
print(words)

for i in my_str:
    if i[::1].replace(' ', '').lower() != i[::-1].replace(' ', '').lower():
        my_str.remove(i)
print(my_str)

