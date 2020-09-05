import sys
import random
from statistics import mean

def main():
    print(
"""
D&D Dice Roller, v1.0
Welcome, adventurer!
Input the die you need to roll as an integer, then the
number of rolls you need.
-- Ex. If you need to roll a d20 once, enter '20', then '1'
-- To Quit, enter '0'
"""
    )

    program_active = True
    rolls = []
    # valid_rolls = [100, 20, 12, 10, 8, 6, 4, 3] currently unused
    while program_active:
        dice = choose_dice()
        num_rolls = choose_num_rolls(dice)

        #  calls roll function x times per user input, num_dice
        for _ in range(num_rolls):
            roll(dice, rolls)

        if num_rolls == 1:
            if rolls[0] == 20:
                print("* * NATURAL 20 * *")
                print(f"\nRoll: {rolls[0]}")
                print("----------")
            elif rolls[0] == 1:
                print(". . Natural 1 . .")
                print(f"\nRoll: {rolls[0]}")
                print("----------")
            else:
                print(f"\nRoll: {rolls[0]}")
                print("----------")
        else:
            print(f"\nRolls: {rolls}")
            print("Sum:", sum(rolls))
            print("Average:", round(mean(rolls), 2))
            print("----------")

        rolls.clear()  # clears list of rolls

def choose_dice():
    """User inputs required dice-type to be rolled.
    Input: Input integer. If d20 needed, input '20'. If d6 needed, '6'. '0' is Quit.
      Returns: Returns dice as an integer or Quits.
    """
    while True:
        try:
            dice = input("\nRoll... ")
            dice = int(dice)
            break
        except ValueError:
            print("Are you scared, peasant? Roll again...")

    if dice == 0:
        print("\nFare thee well.")
        sys.exit()
    else:
        return dice

def choose_num_rolls(dice):
    """User inputs required number of rolls for selected dice-type. '0' is Quit.
    Input: Input integer for number of rolls required. If 0 is input, program quits.
        Returns: Returns number of rolls required as an integer.
    """
    while True:
        try:
            num_rolls = input(f"How many rolls?... ")
            num_rolls = int(num_rolls)
            break
        except ValueError:
            print("Inconceivable! Feed me integers!")

    if num_rolls == 0:
        print("\nFare thee well.")
        sys.exit()
    else:
        return num_rolls

def roll(dice, rolls):
    """Lists available dice, generates random number(s), adds number(s) to list.
    Input: Takes prompted user input of dice type required.
        Returns: Random number based on selected dice type.
    """
    random_roll = random.randint(1, dice)
    rolls.append(random_roll)


main()
