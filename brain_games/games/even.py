import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def challenge():
    number = random.randint(1, 100)
    if is_even(number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number


def is_even(number):
    return True if number % 2 == 0 else False
