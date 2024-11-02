# prompt: Simulate rolling two dice, three times.  Prints the results of each die roll. 

import random

def roll_dice():
  """Simulates rolling two dice and returns the results."""
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  return die1, die2

# Roll the dice three times and print the results
for _ in range(3):
  roll1, roll2 = roll_dice()
  print(f"Die1 : {roll1}, Die2 : {roll2}")


Solution
Die1 : 1, Die2 : 3
Die1 : 5, Die2 : 2
Die1 : 3, Die2 : 4
