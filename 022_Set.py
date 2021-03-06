
# Множество (Set)
# Это списки, элементы ,которых не повторяются
print('*' * 30)
print('Множество (Set)')
print('*' * 30)

# Пример того, что элементы не повторяются
print('- Пример того, что элементы не повторяются')
s = {'apple', 'orange', 'kiwi', 'apple', 'pineapple', 'banana', 'orange'}
print(type(s))
print(s)

# Если строка преобразуется в словарь, то его элементы выводиться в рандомном порядке
print('- Если строка преобразуется в словарь, то его элементы выводиться в рандомном порядке')
s2 = set('hello')
print(s2)

# Если словарь генерируется из последовательности чисел, то его элементы имеют порядок
print('- Если словарь генерируется из последовательности чисел, то его элементы имеют порядок')
s3 = {i for i in range(1, 10 + 1)}
print(s3)

print()
# Пример того, как быстро избавиться от повторяющихся элементов в словаре
print('- Пример того, как быстро избавиться от повторяющихся элементов в словаре')
nums = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8]
nums2 = set(nums)
print(nums2)

nums3 = list(nums2)
print(nums3)
