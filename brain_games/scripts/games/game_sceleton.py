import prompt


def game_structure(game_name, elements):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game_name)
    for i in range(3):
        quest, correct_answ = elements()
        print(f"Question: {quest}")
        answ = prompt.string("Your answer: ")
        if answ == str(correct_answ):
            print("Correct!")
            if i == 2:
                print(f"Congratulations, {name}!")
        if answ != str(correct_answ):
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{correct_answ}'.")
            print(f"Let's try again, {name}!")
            break
        



 


