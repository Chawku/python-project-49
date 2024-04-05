import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def challenge():
    number = random.randint(1, 100)
    if is_prime(number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
