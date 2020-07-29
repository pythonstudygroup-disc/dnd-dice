import sys
import random
from statistics import mean

print("Welcome, brave sir or madam or person!"
      "\n\nInput the die you need to roll as an integer, then the number of"
      " rolls you need. \n-- Ex. If you need to roll a d20 once, enter '20', then '1'\n-- To Quit, enter '0'")

program_active = True
rolls = []

while program_active:
    def choose_dice():
        '''User inputs required dice-type to be rolled.
        Input: Input integer. If d20 needed, input '20'. If d6 needed, '6'. '0' is Quit.
          Returns: Returns dice as an integer or Quits.
        '''
        try:
            dice = input("\nRoll... ")
            dice = int(dice)
        except ValueError:
            print("Are you scared, peasant? Roll again...")

        if dice == 0:
          print("\nFare thee well.")
          sys.exit()
        else: 
          return dice
    dice = choose_dice()

    def choose_num_rolls(dice):
        '''User inputs required number of rolls for selected dice-type. '0' is Quit.
        Input: Input integer for number of rolls required. If 0 is input, program quits.
            Returns: Returns number of rolls required as an integer.
        '''
        rolls.clear() # clears list of rolls
        try:
            num_rolls = input(f"How many rolls?... ")
            num_rolls = int(num_rolls)
        except ValueError:
            print("Inconceivable! Feed me integers!")
        
        if num_rolls == 0:
          print("\nFare thee well.")
          sys.exit()
        else: 
          return num_rolls
    num_rolls = choose_num_rolls(rolls)
    
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

    #  calls roll function x times per user input, num_rolls
    for _ in range(num_rolls):
        roll(dice)

    if num_rolls == 1:
        if rolls[0] == 20:
            print("* * NATURAL 20 * *")
            print(f"Roll: {rolls[0]}")
            print("----------")
        elif rolls[0] == 1:
            print(". . Natural 1 . .")
            print(f"Roll: {rolls[0]}")
            print("----------")
        else:    
            print(f"Roll: {rolls[0]}")
            print("----------")
    else:
        print(f"Rolls: {rolls}")
        print("Sum:", sum(rolls))
        print("Average:", round(mean(rolls), 2))
        print("----------")
