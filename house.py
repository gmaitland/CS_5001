class House:
    """A class that represents a house"""
    def __init__(self):
        self.bedrooms = 0
        self.kitchens = 0
        self.bathrooms = 0

    def person_cooking(self, time): # In minutes
        """An instance method that represents a cooking function"""
        self.cooking_time = 0
        print(f'A person is cooking for {self.cooking_time} minutes')

    def person_showering(self, time):
        """An instance method that represents a showering function"""
        self.showering_time = 0
        print(f'A person is showering for {self.showering_time} minutes')

    def house_status(self):
        """An instance method that returns the updated details of the house"""
        print(f'The house has {self.bedrooms} bedrooms', end=' ')
        print(f'{self.kitchens} kitchens, {self.bathrooms} bathrooms')
        print(House.person_cooking())
        print(House.person_showering())


my_house = House()
my_house.bedrooms = 3
my_house.kitchens = 1
my_house.bathrooms = 1

my_house.person_cooking(5)

my_house.person_showering(15)

my_house.house_status()
