import random

game_name = 'Answer "yes" if the number is even, otherwise answer "no".'


def elements():
    a = random.randint(0, 1000)
    if a % 2 == 0:
        cr_an = "yes"
    else:
        cr_an = "no"
    quest = a
    return (quest, cr_an)