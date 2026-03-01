import random

game_name = "What is the result of the expression?"


def elements():
    a = random.randint(0, 1000)
    b = random.randint(0, 1000)
    operator = random.choice(["+", "-", "*"])
    if operator == "+":
        correct_answ = a + b
    if operator == "-":
        correct_answ = a - b
    if operator == "*":
        correct_answ = a * b
    quest = f"{a} {operator} {b}"
    return (quest, correct_answ)