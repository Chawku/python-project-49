import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    number = random.randint(1, 100)

    if number > 1:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return correct_answer, number
