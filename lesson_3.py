from enum import Enum


class Color(Enum):
    BLUE = '\33[34m'
    YELLOW = '\33[33m'
    DARK_RED = '\33[31m'


class Drawable:
    def draw(self, emoji):
        print(emoji)


class MusicPlayable:
    # def __init__(self):
    #     pass

    def play_music(self, song):
        print(f"Now is playing {song}")

    def stop_music(self):
        print('Music stopped')


class SmartPhone(MusicPlayable, Drawable):
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if type(color) == Color:
            self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return (f'MODEL: {self.__model} YEAR: {self.__year} '
                f'COLOR: {self.__color.value}{self.__color.name}'
                + '\33[0m')

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year


class FuelCar(Car):
    __total_fuel_amount = 1000

    @staticmethod
    def get_fuel_type():
        return 'AI - 98'

    @classmethod
    def get_total_fuel_amount(cls):
        return cls.__total_fuel_amount

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel_amount += amount

    def __init__(self, model, year, color, fuel_bank):
        # super().__init__(model, year, color)
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel')

    def __str__(self):
        return super().__str__() + f' FUEL BANK: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by electricity')

    def __str__(self):
        return super().__str__() + f' BATTERY: {self.__battery}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)


# some_car = Car('Ford Mustang', 2022, 'red')
# print(some_car)

print(f'Fabric FUEL_CAR has: {FuelCar.get_total_fuel_amount()} '
      f'({FuelCar.get_fuel_type()}) litters.')

camry = FuelCar('Toyota Camry',
                2009, Color.YELLOW, 85)
print(camry)

model_x = ElectricCar('Tesla Model X',
                      2023, Color.BLUE, 25000)
print(model_x)

prius = HybridCar('Toyota Prius',
                  2019, Color.DARK_RED, 70, 15000)
print(prius)
prius.drive()
print(HybridCar.mro())

number_1 = 8
number_2 = 3
print(f'Number one is bigger than number two: {number_1 > number_2}')
print(f'Number one is equal to number two: {number_1 == number_2}')

print(f'Camry is better than prius: {camry > prius}')
print(f'Camry is not the same with prius: {camry != prius}')

print(f'Sum of numbers: {number_1 + number_2}')
print(f'Sum of fuel banks: {camry + prius}')

# FuelCar.total_fuel_amount -= 100
FuelCar.buy_fuel(500)
print(f'Fabric FUEL_CAR has: {FuelCar.get_total_fuel_amount()} '
      f'({FuelCar.get_fuel_type()}) litters.')

camry.play_music('Best song')

samsung = SmartPhone()
samsung.play_music('Tra la la')
samsung.stop_music()

camry.draw('🚗')
samsung.draw('📱')

if model_x.model == 'Tesla Model x':
    print('This car is cool!')

if model_x.color == Color.BLUE:
    print('This car is beautiful')
