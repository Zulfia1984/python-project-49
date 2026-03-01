import random

game_name = "What number is missing in the progression?"

def elements():
    n = random.randint(5, 10)
    d = random.randint(1, 10)
    f = random.randint(1, 20)
    sp = [str(f)]
    for j in range(1, n):
        m=f+d*j
        sp.append(str(m))
    x=random.randint(0, n-1)
    correct_answ = sp[x]
    sp[x] = ".."
    quest = ", ".join(sp)
    return(quest, correct_answ)
