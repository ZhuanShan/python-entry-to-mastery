# 9-13
from collections import OrderedDict

favorite_bike = OrderedDict()           #python3.6之后字典默认有序


# 9-14

from random import randint
x = randint(1, 6)

class Die():
    def __init__(self) -> None:
        self.sides = 6

    def roll_die(self):
        print(randint(1,self.sides))

d1 = Die()
for i in range(10):
    d1.roll_die()


