import random
import math

print("Welcome, brave sir or madam or person! Choose your weapon..."
      "\n\nInput the dice you need to roll as an integer."
      "\n\nie. If you need to roll a d20, type '20')")

while True:
    try:
        dice = int(input("Roll... "))
        dice = int(dice)
        break
    except ValueError:
        print("Are you scared, peasant? Please roll again...")

def roll(dice):
    '''Generates a random dice roll for major D&D dice.

    Input: An integer such as 20 for a d20, 100 for d100, etc.
    Output: Prints for user and returns dice roll result for later use.
    '''
    if dice == 100:
        random100 = math.floor(random.random() * 100 + 1)
        print(random100)
        return random100
    elif dice == 20:
        random20 = math.floor(random.random() * 20 + 1)

        if random20 == 20:
            print(f"Natural 20! Critical Success!!!")
        elif random20 == 1:
            print("Natural 20! Pray to your god(s).")
        else:
            print(random20)

        return random20

    elif dice == 12:
        random12 = math.floor(random.random() * 12 + 1)
        print(random12)
        return random12
    elif dice == 10:
        random10 = math.floor(random.random() * 10 + 1)
        print(random10)
        return random10
    elif dice == 8:
        random8 = math.floor(random.random() * 8 + 1)
        print(random8)
        return random8
    elif dice == 6:
        random6 = math.floor(random.random() * 6 + 1)
        print(random6)
        return(random6)
    elif dice == 4:
        random4 = math.floor(random.random() * 4 + 1)
        print(random4)
        return random4
    elif dice == 3:
        random3 = math.floor(random.random() * 3 + 1)
        print(random3)
        return random3
    elif dice == 000:
        print("You've escaped.")
        return
    else:
        print("Invalid number")
        return

roll(dice)
