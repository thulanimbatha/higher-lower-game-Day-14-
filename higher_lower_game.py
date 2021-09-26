from game_data import data
from art import logo, vs
import random

A = random.choice(data)
B = random.choice(data)

continue_game = True
score = 0

def check_answer(user_guess, accountA, accountB, score):

    if user_guess == 'A':
        if accountA['follower_count'] > accountB['follower_count']:
            # 4 - if user correct, add new option, increment score
            print("You got it right!")
            return True
        else:
            # 5 - if not correct, display score, exit
            print(f"You got it wrong! Your score is: {score}")
            return False

    elif user_guess == 'B':
        if accountA['follower_count'] < accountB['follower_count']:
            # 4 - if user correct, add new option, increment score
            print("You got it right!")
            return True
        else:
            # 5 - if not correct, display score, exit
            print(f"You got it wrong! Your score is: {score}")
            return False

def update_score(condition, score):
    if condition == True:
        return score + 1

def check_equality(account_A, account_B):
    if account_A == account_B:
        return random.choice(data)
    return account_B

'''PROGRAM START'''
while continue_game:

    B = check_equality(A, B)

    name1 = A['name']
    description1 = A['description']
    country1 = A['country']

    name2 = B['name']
    description2 = B['description']
    country2 = B['country']

    # 1 - Print comparisons
    print(logo)

    print(f"Score: {score}")

    print(f"Compare A: {name1}, {description1}, from {country1}")

    print(vs)

    print(f"Against B: {name2}, {description2}, from {country2}")

    # 2 - User makes choice/guess
    user_guess = input("Who has the most followers (type 'A' or 'B')? ").upper()
    
    # 3 - Check -> is User correct?
    continue_game = check_answer(user_guess, A, B, score)

    # 4 - update score
    score = update_score(continue_game, score)

    # 6 - add new option, do not change both options
    if continue_game:
        if user_guess == 'A':
            B = random.choice(data)
        elif user_guess == 'B':
            A = random.choice(data)

