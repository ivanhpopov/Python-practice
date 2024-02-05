from random import randint


class Die:
    def __init__(self, sides):
        """Initialize name and cuisine type"""
        self.sides = sides
    
    def roll_die(self, sides):
        for i in range(1, sides):
            roll = randint(1, 6)
            print(roll)
        
        

        
dice = Die(6)
dice.roll_die(11)
        