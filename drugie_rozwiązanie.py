import random

possible_dices = {"D3": 3,
                  "D4": 4,
                  "D6": 6,
                  "D8": 8,
                  "D10": 10,
                  "D12": 12,
                  "D20": 20,
                  "D100": 100}


def calculate_value(dice_code):
    # program try fin index D
    d_index = dice_code.index('D')
    # check appears sign + or - in dick code. If sign is in dick code program return sign_index
    if '-' in dice_code:
        sign_index = dice_code.index('-')
    elif '+' in dice_code:
        sign_index = dice_code.index('+')
    else:
        sign_index = 0

    # check number of throws
    if d_index == 0:
        throws = 1
    else:
        throws = int(dice_code[0:d_index])

    # chck type of dice
    if sign_index > 0:
        dice_type = dice_code[d_index:sign_index]
    else:
        dice_type = dice_code[d_index:]

    # program identify modificator
    if '+' in dice_code or '-' in dice_code:
        modificator = dice_code[sign_index:]
    else:
        modificator = '0'
    result = 0

    # check dice and main loop
    if dice_type in possible_dices.keys():
        for _ in range(0, throws):
            throw_result = random.randint(1, possible_dices[dice_type])
            result += throw_result
    else:
        return 'Błędna wartość kości'

    # add or subtract modificator
    if modificator != '0' and modificator[0] == '+':
        result += int(modificator[1:])
    elif modificator != '0' and modificator[0] == '-':
        result -= int(modificator[1:])
    return result



