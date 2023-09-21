#
# dice.py
#
# Created by Persephone on 21.09.23 at 16.07
#
from random import randint

class Dice():

    def __init__(self, foo):
        self.foo = foo

    def roll(self):
        result = randint(1,self.foo)
        return result
 
d20 = Dice(20)
d12 = Dice(12)
dper = Dice(100)
d10 = Dice(10)
d8 = Dice(8)
d6 = Dice(6)
d4 = Dice(4)
d2 = Dice(2)
