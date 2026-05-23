import random
def dice_type(sides):
    roll = random.randint(1, sides)
    return roll

print(dice_type(8))