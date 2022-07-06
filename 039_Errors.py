import sys

# Обработка ошибок
print('*' * 10)
print('First task')
print('*' * 10)


# Попытаемся прочитать файл, которого не существует (перехватим все ошибки, которые могут быть)
print('- Попытаемся прочитать файл, которого не существует (перехватим все ошибки, которые могут быть - Exception)')

# ./workdir/passwords.txt
input_file = input('Введите правильный путь к файлу: ')

while True:
    try:
        input_file_pointer = open(input_file, mode='r', encoding='utf-8')
    except Exception:
        print(f'Some error in file - {input_file}')
        # Выводим часть самой ошибки, которая представленна в 1-ом элементе массива
        print(sys.exc_info()[1])
        # "sys.exit()" используется, чтобы прекратить выполнять код при ошибке
        #sys.exit()
        input_file = input('Введите правильный путь к файлу: ')
    else:
        print(input_file_pointer.read())
        break

