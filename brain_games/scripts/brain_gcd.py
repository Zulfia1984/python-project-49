import prompt

import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")
    for i in range(3):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        z = min(a, b)
        for i in range(z, 0, -1):
            if a%i==0 and b%i==0:
                correct_answ = i
                break
        quest = str(a)+ " "+str(b)
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
        

    
    
             

