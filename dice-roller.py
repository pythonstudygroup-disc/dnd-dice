import random
import math
# 
#
#
print("Welcome, brave sir or madam or person! Choose your weapon..."
      "\n\nInput the die you need to roll as an integer."
      "\n\nie. If you need to roll a d20, type '20')")
while True:
    try:
        dice = int(input("Roll... "))
        dice = int(dice)
        break
    except ValueError:
        print("Are you scared, peasant? Please roll again...")
		

def roll(dice):
	valid_rolls = [20,12,10,8,6,4,3]
	if dice in valid_rolls:
		random_roll = math.floor(random.random() * dice + 1)
		print(random_roll)
	else:
		print("not a valid rolls")
roll(dice)		
