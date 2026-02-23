import prompt

import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    for i in range(3):
        a = random.randint(0, 1000000)
        print(f"Question: {a}")
        answ = prompt.string("Your answer: ")
        if (a%2==0 and answ.lower()=="yes") or (a%2==1 and answ.lower()=="no"):
            print("Correct!")
            if i==2:
                print(f"Congratulations, {name}!")
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break