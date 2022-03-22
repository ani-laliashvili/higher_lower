from art import logo, vs
from game_data import data
import random

def check_answer(guess, a, b, score):
    """
    Checks guess against the answer
    :param guess: user guess
    :param a: first account
    :param b: second account
    :param score: user score so far
    """
    if guess == 'A' and a['follower_count'] > b['follower_count']:
        higher_lower(a, score + 1)
    elif guess == 'B' and b['follower_count'] > a['follower_count']:
        higher_lower(b, score + 1)
    else:
        print(f'Sorry, that\'s wrong. Final score: {score}')


def higher_lower(a, score):
    """
    Allows user to play a Higher Lower game
    :param a:
    :param score: number of correct guesses so far
    """
    print('\n'*50)
    print(logo)
    if a == '':
        a = random.choice(data)
    else:
        print(f'You\'re right. Current score: {score}')
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")

    print(vs)
    b = random.choice(data)
    if a == b:
        b = random.choice(data)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

    check_answer(input('Who has more followers? Type \'A\' or \'B\': '), a, b, score)

if __name__ == '__main__':
    higher_lower('', 0)
