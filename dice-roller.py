import random
from statistics import mean

print("Welcome, brave sir or madam or person!"
      "\n\nInput the die you need to roll as an integer, then the number of"
      " rolls you need. ie. If you need a d20, enter 20.")

rolls = []

#    prompts user to enter which die to roll
while True:
    try:
        dice = int(input("Roll... "))
        dice = int(dice)
        break
    except ValueError:
        print("Are you scared, peasant? Roll again...")

#    number of rolls with required die
while True:
    try:
        num_dice = int(input(f"How many d{dice}'s?... "))
        num_dice = int(num_dice)
        break
    except ValueError:
        print("That's not possible. Feed me integers!")

def roll(dice):
    '''Lists available dice, generates random number(s), adds number(s) to list.

    Input: Takes prompted user input of dice type required.
        Returns: Random number based on selected dice type.
    '''
    valid_rolls = [100, 20, 12, 10, 8, 6, 4, 3]
    if dice in valid_rolls:
        random_roll = random.randint(1, dice)
        rolls.append(random_roll)
    else:
        print("Not a valid roll.")

#   calls roll function x times per user input, num_dice
for _ in range(num_dice):
    roll(dice)

#   handles and outputs number of rolls as required by user
if num_dice == 1:
    print(f"Roll: {rolls[0]}")
else:
    print(f"Roll(s): {rolls}")
    print("Sum:", sum(rolls))
    print("Average:", round(mean(rolls), 2))

# TO DO
# Add if / else for d20: congrats if natural 20, response for natural 1
# Create loop after initialization so you don't have to Run each time
