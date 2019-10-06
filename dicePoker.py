from random import randrange

# The dice class which contains the scoring system
class Dice:
  def __init__(self):
    self.dice = [0]*5
    self.rollDice()
    
  def roll(self,which):
    for i in which:
      self.dice[i] = randrange(1,7)
  
  def rollDice(self):
    self.roll(range(5))
    
  def values(self):
    return self.dice[:]
  
  def score(self):
    counts = [0]*7
    for value in self.dice:
      counts[value] = counts[value] + 1
    
    # pay system  
    if 5 in counts:
      return "Five of a kind", 30
    elif 4 in counts:
      return "Four of a kind", 15
    elif (3 in counts) and (2 in counts):
      return "Full House", 12
    elif not (2 in counts) and (counts[1]==0 or counts[6]==0):
      return "Straight", 20
    elif counts.count(2) == 2:
      return "Two Pairs", 5 
    else:
      return "Loss", 0

class PokerApp:
  def __init__(self,interface):
    self.dice = Dice()
    self.money = 100
    self.interface = PokerInterface()

  def run (self) :
    while self.money >= 10 and self.interface.Play():
      self.playRound()
      self.interface.close()
# Enable the player to play more than one round
  def playRound(self):
    self.money = self.money - 10
    self.interface.setMoney(self.money)
    self.doRolls()
    result,score = self.dice.score()
    self.interface.showResult(result,score)
    self.money = self.money + score
    self.interface.setMoney(self.money)

  def doRolls(self):
    self.dice.rollDice()
    roll = 1
    self.interface.setDice(self.dice.values())
    toRoll = self.interface.chooseDice()
    while roll < 3 and toRoll != []:
      self.dice.roll(toRoll)
      roll = roll + 1
      self.interface.setDice(self.dice.values())
      if roll < 3:
        toRoll = self.interface.chooseDice()

class PokerInterface:
  def __init__(self):
    print("Welcome to dice poker.")
  def setMoney (self,amount):
    print ("You currently have R{0}.".format(amount))
  def setDice (self,values):
    print("Dice:",values)
  def Play (self):
    answer = input ("Want to play? ")
    return answer in " yY"
  def close(self):
    print ("\nThank you for playing!")
  def showResult(self,msg,score):
    print("{}.You win R{}.".format(msg,score))
  def chooseDice(self):
    return eval(input("Enter list of which position to change ([] to stop)"))


interface = PokerInterface()
app = PokerApp(interface)
app.run()

