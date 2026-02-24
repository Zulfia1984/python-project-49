import prompt

import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    for i in range(3):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        operator = random.choice(["+", "-", "*"])
        if operator=="+":
            correct_answ=a+b
        if operator=="-":
            correct_answ=a-b
        if operator=="*":
            correct_answ=a*b
        quest=f"{a} {operator} {b}"
        print(f"Question: {quest}")
        answ = prompt.string("Your answer: ")
        if answ == str(correct_answ):
            print("Correct!")
            if i==2:
                print(f"Congratulations, {name}!")
        if answ != str(correct_answ):
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{correct_answ}'.")
            print(f"Let's try again, {name}!")
            break
        

