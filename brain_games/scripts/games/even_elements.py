import random

game_name = "Answer 'yes' if the number is even, otherwise answer 'no'."


def elements():
    a = random.randint(0, 1000)
    if a % 2 == 0:
        correct_answ = "yes"
    else:
        correct_answ = "no"
    quest = a
    return (quest, correct_answ)