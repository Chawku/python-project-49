import random
from math import gcd

RULES = 'Find the greatest common divisor of given numbers.'


def challenge():
    first = random.randint(0, 100)
    second = random.randint(0, 100)

    question = f'{first} {second}'
    correct_answer = str(gcd(first, second))
    return correct_answer, question
