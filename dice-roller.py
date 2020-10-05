import random
import sys
from statistics import mean


def welcome():

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


def quit_():
    """Quit program; exit loop by user input of '0' during any prompt.
    
    Prints: Message and sys.exit().
    """
    print("\nFare thee well.")
    sys.exit()


# Handle dice
def dice_input():
    """Called from handle_dice_input to take user input for their dice
    selection. Separate function for pytest / monkeypatching purposes.
    
    Input: User input, a whole number as their dice selection. Ex. '20'
    to roll a d20, '8' to roll a d8, '100' to roll a d100.

    Returns: dice, sends user's dice selection to handle_dice_input.
    """
    dice = input("\nRoll... ").strip()
    return dice


def hidden_button():
    """A shortcut within handle_dice_input to roll a d20.
    
    Prints: A random integer from 1 to 20.
    """
    random_20 = random.randint(1, 20)
    print(random_20)


def handle_dice_input():
    """User input from dice_input for dice selection is handled.
        - If 0, quit_()
        - If "", hidden_button()
        - If non-int, error handle and request new user input.
        
    Returns: dice, if non-zero and an integer.
    """
    while True:
        try:
            dice = dice_input()
            dice = int(dice)
            # go to choose_num_dice or quit_()
            if dice == 0:
                quit_()
        except ValueError:
            # go to hidden_button
            if dice == "":
                hidden_button()
            else:
                print("Are you scared, peasant? Roll again...")
        else:
            return dice


# Handle rolls
def roll_input():
    """Called from handle_num_rolls to take user input for their dice
    selection. Separate function for pytest / monkeypatching purposes.

    Input: User input, a whole number as their number of rolls required.

    Returns: num_rolls, sends user's number of rolls to handle_num_rolls.
    """
    num_rolls = input(f"How many rolls?... ").strip()
    return num_rolls


def handle_num_rolls():
    """User input from roll_input for requested number of rolls is handled.
        - If 0, quit_()
        - If non-int, error handle and request new user input.
        
    Returns: num_rolls, if a non-zero and an integer
    """
    while True:
        try:
            num_rolls = roll_input()
            num_rolls = int(num_rolls)
            if num_rolls == 0:
                quit_()
        except ValueError:
            print("Inconceivable! Feed me integers!")
        else:
            return num_rolls


def if_num_rolls_one(dice):
    """Creates a blank list of one roll, has roll function generate a random
    number,	then outputs information to user.

    Input: dice, an integer

    Prints: The roll and prints a unique messages if dice was a d20 and
    roll was a 1 or 20.
    """
    rolls = []
    roll(dice, rolls)
    if rolls[0] == 20 and dice == 20:
        print("* * NATURAL 20 * *")
        print(f"\nRoll: {rolls[0]}")
        print("----------")
    elif rolls[0] == 1 and dice == 20:
        print(". . Natural 1 . .")
        print(f"\nRoll: {rolls[0]}")
        print("----------")
    else:
        print(f"\nRoll: {rolls[0]}")
        print("----------")

    rolls.clear()


def if_num_rolls_more(dice, num_rolls):
    """Creates a blank list of more than one roll, has roll function generate
    rolls, then outputs information to user.
    
    Args:
        - dice, an integer
        - num_rolls, an integer

    Prints: information to user; the rolls, the sum of the rolls, and the
    average of the rolls.
    """
    rolls = []

    for _ in range(num_rolls):
        roll(dice, rolls)

    print(f"\nRolls: {rolls}")
    print("Sum:", sum(rolls))
    print("Average:", round(mean(rolls), 2))
    print("----------")

    rolls.clear()


def handle_both(dice, num_rolls):
    """Invokes appropriate roll function depending on whether user needs
    one or more rolls.
    
    Args:
        - dice, an integer
        - num_rolls, an integer

    Returns: No return.
    """
    if num_rolls > 1:
        if_num_rolls_more(dice, num_rolls)
    else:
        if_num_rolls_one(dice)


def roll(dice, rolls):
    """Lists available dice, generates random number(s), adds number(s) to
    list.

    Args:
        - dice, an integer
        - rolls, an empty list to populate

    Returns: No return, but appends list to be handled by if_num_rolls_more or
        if_num_rolls_one.
    """
    random_roll = random.randint(1, dice)
    rolls.append(random_roll)


def run_program():
    """Welcome message and runs program.

    Note: Program continues until user chooses to quit_() with input of '0' during
    any input prompt.
    """
    welcome()
    program_active = True

    while program_active:
        dice = handle_dice_input()
        num_rolls = handle_num_rolls()
        handle_both(dice, num_rolls)


run_program()
