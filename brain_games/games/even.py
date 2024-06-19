import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def challenge():
    random_number = random.randint(1, 100)
    if is_even(random_number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, random_number


def is_even(random_number):
    return True if random_number % 2 == 0 else False
