from random import randint

class Dice:
    """ A class representing a single die that can be rolled to generate random numbers."""
    def __init__(self):
        self.side = 6
        self.number_of_roll = 0

    def roll_dice(self):
        for _ in range(self.number_of_roll):
            print(randint(1,self.side))

    def set_sides(self):
        self.side = int(input('Set the number of side of dice: '))

    def set_number_of_roll(self):
        self.number_of_roll = int(input('Set the number of rolls: '))

    def play(self):
        self.set_sides()
        self.set_number_of_roll()
        self.roll_dice()

my_dice = Dice()
my_dice.play()
