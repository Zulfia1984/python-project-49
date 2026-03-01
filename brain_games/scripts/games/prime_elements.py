import random

game_name = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def elements():
    a = random.randint(1, 1000)
    for i in range(2, a):
        if a % i == 0:
            correct_answ = "no"
            break
        else:
            correct_answ = "yes"
    
    quest = a
    return (quest, correct_answ)