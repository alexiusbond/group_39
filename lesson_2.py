class Contact:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number


class Animal:
    def __init__(self, name, age, contact_info):
        self.__name = name
        self.__age = age
        if isinstance(contact_info, Contact):
            self.__contact_info = contact_info
        else:
            raise ValueError('Invalid contact. It must be of data type Contact')
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born!')

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if type(new_age) != int or new_age <= 0:
            raise ValueError('Invalid age. It must be positive number')
        else:
            self.__age = new_age

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def info(self):
        return (f'NAME: {self.__name}, AGE: {self.__age} BIRTH YEAR: {2024 - self.__age} '
                f'\nCONTACT INFO: {self.__contact_info.city}, {self.__contact_info.street}'
                f' {self.__contact_info.number}')

    def make_voice(self):
        raise NotImplementedError('Method make_voice must be implemented')


class Fish(Animal):
    def __init__(self, name, age, contact_info):
        super(Fish, self).__init__(name, age, contact_info)

    def make_voice(self):
        pass

class Cat(Animal):
    def __init__(self, name, age, contact_info):
        super(Cat, self).__init__(name, age, contact_info)

    def make_voice(self):
        print('Myauu')


class Dog(Animal):
    def __init__(self, name, age, commands, contact_info):
        # super().__init__(name, age)
        super(Dog, self).__init__(name, age, contact_info)
        self.__commands = commands

    # getter
    @property
    def commands(self):
        return self.__commands

    # setter
    @commands.setter
    def commands(self, value):
        self.__commands = value

    # method overriding
    def info(self):
        return super().info() + f'\nCOMMANDS: {self.__commands}'

    def make_voice(self):
        print('Gav')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contact_info):
        super(FightingDog, self).__init__(name, age, commands, contact_info)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f'\nWINS: {self.__wins}'

    def make_voice(self):
        print('Rrrrr gav')


# some_animal = Animal('Anim', 2)
# some_animal.__age = 'Five years old'
# some_animal.set_age(4)
# print(some_animal.get_age())
# print(some_animal.info())

contact_1 = Contact('Bishkek', 'Toktogula', 1)

cat = Cat('Tom', 6, contact_1)
# print(cat.info())

dog = Dog('Frank', 1, 'Sit', contact_1)
# print(dog.commands)
dog.commands = 'Sit, bark'
# print(dog.info())

#       a = b
contact_2 = Contact('Osh', 'Lenina', 5)

fightingDog = FightingDog('Pushok', 3, 'Fight', 7,
                          Contact('Osh', 'Lenina', 5))
# print(fightingDog.info())

# print('---------------------')
# contact_1.street = 'Aidemira'
#
# print(cat.info())
# print(dog.info())

fish = Fish('Nemo', 4, contact_1)

animals_list = [fish, cat, dog, fightingDog]
for animal in animals_list:
    print(animal.info())
    animal.make_voice()
