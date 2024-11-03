# Simulate rolling two dice, and prints results of each roll as well as the total manually.
# simulating by taking two random numbers from 1 to 6 and adding them.

die1 : int = input("Select any number from 1 to 6 for die 1: ")
die2 : int = input("Select any number from 1 to 6 for die 2: ")

total : int = int(die1) + int(die2)

print(f"Die 1 : {die1}, Die 2 : {die2}, Total : {total}")

Solution
Select any number from 1 to 6 for die 1: 4
Select any number from 1 to 6 for die 2: 6
Die 1 : 4, Die 2 : 6, Total : 10



# Simulate rolling two dice, and prints results of each roll as well as the total by importing random

import random

Numsides = 6

die1 = random.randint(1,Numsides)
die2 = random.randint(1,Numsides)

print(f"Die 1 : {die1}, Die 2 : {die2}, Total : {die1 + die2}")

Solution
Die 1 : 4, Die 2 : 6, Total : 10
