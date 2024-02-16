class Transport:
    def __init__(self, theModel, theYear, theColor):
        self.model = theModel
        self.year = theYear
        self.color = theColor

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, theModel, theYear, theColor):
        super().__init__(theModel, theYear, theColor)


class Car(Transport):
    # class attribute
    counter = 0
    standard_number_of_wheels = 4

    # constructor           # parameters
    def __init__(self, theModel, theYear, theColor, penalties=0.0):
        # fields/attributes
        super().__init__(theModel, theYear, theColor)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')

    # method
    def signal(self, number_of_times):
        print(f'Car {self.model}', end=' ')
        while number_of_times > 0:
            print(f'BEEEEEP', end=' ')
            number_of_times -= 1
        print('\n')


class Truck(Car):
    standard_number_of_wheels = 12
    def __init__(self, theModel, theYear, theColor, penalties=0.0, load_capacity=0):
        super().__init__(theModel, theYear, theColor, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, type_of_cargo, weight):
        if self.load_capacity < weight:
            print(f'You can not load more than {self.load_capacity} kg.')
        else:
            print(f'You successfully loaded {type_of_cargo} ({weight} kg.) on {self.model}')


price_of_winter_lastic = 5000
print(f'Fabric CAR produced: {Car.counter} cars.')
print(f'We need {Car.standard_number_of_wheels * Car.counter * price_of_winter_lastic} soms.')

bmw_car = Car('BMW X6', 2022, 'Red')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} '
      f'COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'Green'
bmw_car.change_color('Green')
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} '
      f'NEW COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')

honda_car = Car(penalties=1200, theYear=2009, theModel='Honda Fit', theColor='Silver')
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} '
      f'COLOR: {honda_car.color} PENALTIES: {honda_car.penalties}')

bmw_car.drive('Osh')
honda_car.drive('Kant')
honda_car.signal(5)

print(f'Fabric CAR produced: {Car.counter} cars.')
print(f'We need {Car.standard_number_of_wheels * Car.counter * price_of_winter_lastic} soms.')

boeing_plane = Plane('Boeing 337', 2020, 'Blue')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} '
      f'COLOR: {boeing_plane.color}')

kamaz_truck = Truck('Kamaz 200', 2000, 'Orange', 900, 30000)
print(f'MODEL: {kamaz_truck.model} YEAR: {kamaz_truck.year} '
      f'COLOR: {kamaz_truck.color} PENALTIES: {kamaz_truck.penalties} '
      f'LOAD CAPACITY: {kamaz_truck.load_capacity} kg.')
kamaz_truck.load_cargo('potatoes', 45000)
kamaz_truck.load_cargo('tomatoes', 10000)
kamaz_truck.drive('Batken')

print(f'Standard on Truck fabric: {Truck.standard_number_of_wheels}')