import json

# Создадим списки игроков, в которые будут помещены их настройки
settings = './workdir/settings.txt'
settings_pointer = open(settings, mode='w', encoding='utf-8')

player_1 = {
    'Name': 'Donald Trump',
    'Score': 345,
    'awards': ['NY', 'OR', 'NV']
}

player_2 = {
    'Name': 'Hilary Clinton',
    'Score': 202,
    'awards': ['WT', 'TX', 'MI']
}

players = []
players.append(player_1)
players.append(player_2)

# Сохраним настройки в файл в JSON формате

json.dump(players, settings_pointer)
settings_pointer.close()

# Прочитаем настройки из файла
print('- Read settings with JSON')

settings_pointer = open(settings, mode='r', encoding='utf-8')
for i in json.load(settings_pointer):
    print(i)

# Если хотите вывести красиво, то можно так
print('- Если хотите вывести красиво, то можно так')
settings_pointer.seek(0)

for i in json.load(settings_pointer):
    print(f'Player name is {i["Name"]}')
    print(f'He has Score: {i["Score"]}')
    print(f'Player awards: {i["awards"][0]}, {i["awards"][1]}, {i["awards"][2]}')
    print()

settings_pointer.close()