#       Define a class "Dice" , inside it a method called "roll", when we 
#       we call this method, we get a tuple of two random values

import random       # importing the built-in module of python named random

class Dice:
    a = int(random.randint(1,6))
    b = int(random.randint(1,6))
    def roll(self):
        tup = (self.a, self.b)
        return tup


e1 = Dice()
print(e1.roll())