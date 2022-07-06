# Регулярные выражения
print('*' * 30)
print('Регулярные выражения')
print('*' * 30)

import re

# Строки для тестов

s = '''это просто строка текста.
А это еще одна строка текста.
А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10.
имена - Денис, Оля, Никита, Злата
года - 1986, 1987, 2018, 2020
А это строка с разными символами: "!", "@", "-", "&", "?", "_".
a\\b\tc
test string
'''

# Объявляем шаблон (то, что мы ищем)

pattern = r'строка'


# 1-й пример. Если искомое слово (шаблон) встречается хоть один раз, то выводим - "Matched"
print('- 1-й пример. Если искомое слово (шаблон) встречается хоть один раз, то выводим - "Matched"')

if re.search(pattern, s):
    print('Matched')
else:
    print('No Match')


# Вывод служебной информации
print('- Вывод служебной информации')

result = re.search(pattern, s)

print(result)
print(result.start())
print(result.end())
print(result.span())


# Найти все совпадения по шаблону
print('- Найти все совпадения по шаблону')

print(re.findall(pattern, s))


'''
"\w" - короткая запись - "[A-Za-z0-9_]" т.е. все буквы и цифры
"\d" - короткая запись - "[0-9]" т.е. все цифры
"\D" - короткая запись - [^0-9] т.е. все, кроме цифр
"\W" - короткая запись - "[^A-Za-z0-9_]" т.е. все, кроме букв и цифр
"\s" - короткая запись - "[ \f\n\r\t\v]" т.е. пробельные символы
"\S" - короткая запись - "[^ \f\n\r\t\v]" т.е. все, кроме пробельных символов

"+" - одно и более повторений
"*" - ноль и более повторений
"?" - ноль и одно повторение
"{n}", где n - чсло повторений
"{m,n}", где m и n - числа повторений от и до, соответственно

Примеры:
"\d\d\d\d" или "\d{4}" - найти 4 любые цифры идущие подряд
'''


pattern1 = r'\w+'
pattern2 = r'\d+'
pattern3 = r'\d{4}'
pattern4 = r'[А-ЯA-Z][а-яa-z]+'


print('- Ищем буквы и цифры, которые повторяются один и более раз')
print(re.findall(pattern1, s))

print('- Ищем цифры, которые повторяются один и более раз')
print(re.findall(pattern2, s))

print('- Найти 4 любые цифры идущие подряд')
print(re.findall(pattern3, s))

print('- Найти слова, которые начинаются с большой буквы, а далее идут маленькие буквы (имена)')
print(re.findall(pattern4, s))


# Сделаем валидацию email адреса
print()
print('- Сделаем валидацию email адреса')

email = input('Введите свой адрес электронной почты: ')


def validate_email(email):
    match = r'[\w_.-]+@[A-Za-z-]+\.[\w.]+'
    if re.findall(match, email):
        return 'Match'
    else:
        return 'No Match'


print(validate_email(email))



# Сделаем валидацию ip адреса
print()
print('- Сделаем валидацию ip адреса')

ip_address = '192.168.0.1'

def validate_ip(ip_address):
    match = r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
    if re.findall(match, ip_address):
        return 'Match'
    else:
        return 'No Match'

print(validate_ip(ip_address))



# Рабочий пример.
print()
print('- Рабочий пример')

input_file = './workdir/dump.txt'
output_file = './workdir/dump_emails.txt'

input_file_pointer = open(input_file, mode='r', encoding='utf-8')
output_file_pointer = open(output_file, mode='w', encoding='utf-8')

pattern = r'[\w_.-]+@[A-Za-z-]+\.[\w.]+'
# Этот шаблон с исключением домена - "dmail.com"
pattern_with_exclude = r'[\w_.-]+@(?!dmail\.com)[A-Za-z-]+\.[\w.]+'

input_file_pointer.seek(0)

email_counter = 0

for i in re.findall(pattern, input_file_pointer.read()):
    # выведем результат на экран
    print(i)
    # Запишем результат в файл
    output_file_pointer.write(f'{i}\n')
    email_counter += 1

# Выводим количество email ов, которые было найдено
print(f'All emails: {email_counter}')

# Запишем количество email ов, которые было найдено
input_file_pointer.seek(2)
output_file_pointer.write(f'All emails: {email_counter}')

input_file_pointer.close()
output_file_pointer.close()