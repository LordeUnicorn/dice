from random import randrange

<<<<<<< HEAD

=======
#class definition for an n-sided die

#import packages
>>>>>>> ea786ddadd0ee18c5ab4582853e7592957eade2c

class MultiSidedDie:

  #constructor here
  def __init__(self,sides):
  	self.sides = sides
  	self.value = 1

  #define method 'roll' to roll the MultiSidedDie
  def roll(self):
<<<<<<< HEAD
    self.value = randrange(1,self.sides+1)
    return self.value
=======
  	self.value = randrange(1,self.sides+1)
>>>>>>> ea786ddadd0ee18c5ab4582853e7592957eade2c
  	
  #define method 'get_value' to return the current value of the MultiSidedDie
  def get_value(self):
  	return self.value
  #define method 'set_value' to set the die to a particular value
  def set_value(self,value):
    self.value = value
<<<<<<< HEAD
    return self.value

die1 = MultiSidedDie(6).roll()

die2 = MultiSidedDie(6).roll()
die3 = MultiSidedDie(6).roll()
die4 = MultiSidedDie(6).roll()
die5 = MultiSidedDie(6).roll()

dice = die1,die2,die3,die4,die5
print(dice)


=======

die1 = MultiSidedDie(6)
die1.roll()
print(die1.get_value())
>>>>>>> ea786ddadd0ee18c5ab4582853e7592957eade2c
