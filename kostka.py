import random


def count_result(type_dice, throws = 1, modificator = 0):
    """
    Function have 3 arguments:
    type_dice - it is type of dice. Can be D3, D4, D6, D8, D10, D12, D20, D100. Number after a "D" it is number of dice walls.
    Throws - it is number of throws in one round
    Modificator - it is value to add or subtract to value
    Function returns the drawn value
    """
    dict_dice = {"D3": 3,
                 "D4": 4,
                 "D6": 6,
                 "D8": 8,
                 "D10": 10,
                 "D12": 12,
                 "D20": 20,
                 "D100": 100}

    if type_dice not in dict_dice.keys():
        return "Błedna wartość kości"

    result = 0
    for i in range(0, throws):
        throw_result = random.randint(1,dict_dice[type_dice])
        print(f"Dice {throw_result}")
        result += throw_result
        print("Result {result}")
    result = result + modificator
    return result

print(count_result(type_dice="D20",modificator=-3, throws=2))