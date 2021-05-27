import random
import time
global lower, upper, difficulty, right_answer, attempts_amount, attempts
def ask_bounds():
    global lower, upper, difficulty
    lower = int(input("Lower bound? "))
    upper = int(input("Upper bound? "))
    difficulty = int(input("Difficulty? "))
ask_bounds()
while lower >= upper or difficulty > upper - lower:
    print("Incorrect bounds or difficulty, try again.")
    ask_bounds()
right_answer = random.randint(lower, upper)

attempts = 0
attempts_amount = int((upper - lower)/difficulty)
if attempts_amount > 1:
    print(f"You have {attempts_amount} attempts!")
else:
    print(f"You have {attempts_amount} attempt!")

def guess():
    global right_answer, attempts_amount, attempts
    attempts += 1
    attempts_left = attempts_amount - attempts
    guess = int(input("Guess? "))
    if guess == right_answer:
        print("That was the right number, congrats!")
        print(f"Guessed the number in {attempts} attempts.")
        time.sleep(5)
        quit()
    elif attempts_amount != attempts:
        print(f"Wrong! {attempts_left} attempts left.")
    else:
        if attempts_amount > 1:
            print(f"Out of attempts, the answer was {right_answer}. You had {attempts_amount} attempts.")
            time.sleep(5)
            quit()
        else:
            print(f"Out of attempts, the answer was {right_answer}. You had {attempts_amount} attempt.")
            time.sleep(5)
            quit()

while True:
    guess()
