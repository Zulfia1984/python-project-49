import random

game_name = "Find the greatest common divisor of given numbers."

def elements():
    a = random.randint(0, 1000)
    b = random.randint(0, 1000)
    z = min(a, b)
    for i in range(z, 0, -1):
        if a%i==0 and b%i==0:
            correct_answ = i
            break
    quest = str(a)+ " "+str(b)
    return(quest, correct_answ)
