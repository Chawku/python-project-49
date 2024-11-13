import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    random_number = random.randint(1, 100)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return correct_answer, random_number
