import random

class Dice:
    Min_Value = 1
    Max_Value = 6
    
    def roll(self):
        return random.randint(Dice.Min_Value, Dice.Max_Value)