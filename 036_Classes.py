# Classes
print('*' * 30)
print('Классы')
print('*' * 30)

# Создадим класс с героем видео игры. Созадим методы: показывает параметры героя,
# Увеличивает его уровень, двигает нашего героя
print()
print('*' * 30)
print('Создадим класс с героем видео игры. Созадим методы: показывает параметры героя,'
      'Увеличивает его уровень, двигает нашего героя'
      )
print('*' * 30)



class Hero():
    '''Create a hero for the game'''

    def __init__(self, name, level, race):
        '''Initiate a hero'''
        self.name = name
        self.level = level
        self.race = race
        self.health = 100


    def show_hero(self):
        '''Print all parameters of a hero'''
        desc = (f'{self.name} Level is: {self.level} Race is: {self.race} Health is: {self.health}')
        return desc

    def level_up(self):
        '''Upgrade level of a hero'''
        self.level += 1

    def set_health(self, new_health):
        self.health = new_health

    def moove(self):
        '''Start mooving a hero'''
        mooving = (f'A Hero {self.name} start mooving to ...')
        return mooving


# Создаем объект

hero_1 = Hero('Vurdalak', 5, 'Ork')
hero_2 = Hero('Legolas', 10, 'Elf')

# Используем некоторые методы (функции)

print('- Выведем информацию о первом герое')

print(hero_1.show_hero())

print('- Поднимем уровень второго героя и покажем его описание')

hero_2.level_up()
print(hero_2.show_hero())

print('- Уменьшим здоровье первого героя и покажем его описание')

hero_1.set_health(30)
print(hero_1.show_hero())



# Создадим класс с супергероем, который будет наследовать часть методов из предыдущего класса
print()
print('*' * 30)
print('Создадим класс с супергероем, который будет наследовать часть методов из предыдущего класса')
print('*' * 30)


class SuperHero(Hero):
    '''Create a superhero'''

    def __init__(self, name, level, race, magiclevel):
        '''Initiate a superhero'''
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def make_magic(self):
        '''Use magic'''
        self.magic -= 10

    def show_hero(self):
        '''Print all parameters of a hero'''
        desc = (f'{self.name} Level is: {self.level} Race is: {self.race} Health is: {self.health} Magiclevel is: {self.magiclevel}'
                f' Magic is: {self.magic}')
        return desc


# Создаем объект

super_hero_1 = SuperHero('Zoya', 5, 'Human', 300)
super_hero_2 = SuperHero('Gastelo', 10, 'Human', 200)

# Используем некоторые методы (функции)

print('- Выведем информацию о первом герое')

print(super_hero_1.show_hero())

print('- Поднимем уровень второго героя и покажем его описание')

hero_2.level_up()
print(super_hero_2.make_magic())
print(super_hero_2.show_hero())