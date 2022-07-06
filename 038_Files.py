# Работа с файлами
print('*' * 30)
print('Работа с файлами')
print('*' * 30)


# Чтение файла
print()
print('*' * 30)
print('Чтение файла')
print('*' * 30)

# Прочтем некоторый файл
print('- Прочтем некоторый файл')

user_names = './workdir/user_names.txt'

user_names_pointer = open(
    user_names,
    mode='r',
    encoding='utf-8'
)

print(user_names_pointer.read())

# Прочтем некоторый файл по строчно. То, что применяется чаще всего.
print('- Прочтем некоторый файл по строчно. То, что применяется чаще всего.')

# Переместить курсор к началу файла (чтобы python смог еще раз его прочитать)
user_names_pointer.seek(0)

for line in user_names_pointer:
    print(f'Hello, {line.strip()}!')


# Пронумеруем строчки файла
print('- Пронумеруем строчки файла')

user_names_pointer.seek(0)

for index, line in enumerate(user_names_pointer, start=1):
    print(f'{index}: {line.strip()}!')


# Напечатаем строчки, где есть имя - "kristy"
print('- Напечатаем строчки, где есть имя - "kristy"')

user_names_pointer.seek(0)

for line in user_names_pointer:
    if 'kristy' in line:
      print(line.strip())

# После того, как с файлом поработали, лучше его закрыть
user_names_pointer.close()



# Запись в файл
print()
print('*' * 30)
print('Запись в файл')
print('*' * 30)


# Создадим файл с именем - weak_passwords.txt и запишем туда строчки с паролем - "password", которые будут найдены
#  в файле - passwords.txt
print('- Создадим файл с именем - weak_passwords.txt и запишем туда строчки с паролем - "password", которые будут найдены'
      'в файле - passwords.txt')

passwords = './workdir/passwords.txt'
weak_passwords_output = './workdir/weak_passwords.txt'

passwords_pointer = open(passwords, mode='r', encoding='utf-8')
# Создастся пустой файл (если он есть, то удалится старый файл и создасться новый пустой файл)
weak_passwords_pointer = open(weak_passwords_output, mode='w', encoding='utf-8')

weak_string_counter = 0
for index, line in enumerate(passwords_pointer, start=1):
    if 'password' in line:
      weak_string_counter += 1
      print(f'{index}: {line.strip()}')
      weak_passwords_pointer.write(f'{index}: {line}')
print(f'Всего - {weak_string_counter} строк')
# Перемещаем курсор в конец файла (чтобы дописать сумму найденных строк)
weak_passwords_pointer.seek(0, 2)
weak_passwords_pointer.write(f'Всего - {weak_string_counter} строк')

passwords_pointer.close()
weak_passwords_pointer.close()

# Создадим файл с именем - weak_passwords.txt и запишем туда строчки с паролем - "password", которые будут найдены
#  в файле - passwords.txt
print('- Создадим функцию, которая будет создавать файл с именем - weak_passwords_adds.txt и'
      'записывать туда строчки с паролями, которые будут найдены'
      'в файле - passwords.txt. Тут мы посмотрим как дописывать в файл.')

def search_weak_passwords(input, output, search_password):
    input_pointer = open(input, mode='r', encoding='utf-8')
    # Создастся пустой файл (если он есть, создаваться не будет, а будет дописываться туда)
    output_pointer = open(output, mode='a', encoding='utf-8')

    for index, line in enumerate(input_pointer, start=1):
        if search_password in line:
            print(f'{index}: {line.strip()}')
            output_pointer.write(f'{index}: {line}')
    input_pointer.close()
    output_pointer.close()

search_weak_passwords('./workdir/passwords.txt', './workdir/weak_passwords_add.txt', 'password')
search_weak_passwords('./workdir/passwords.txt', './workdir/weak_passwords_add.txt', 'vasya')