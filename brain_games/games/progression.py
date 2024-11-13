import random

RULES = 'What number is missing in the progression?'


def generate_question():
    number = random.randint(1, 30)
    difference = random.randint(1, 30)
    length = 10

    progression = [number + i * difference for i in range(length)]

    random_index = random.randint(0, length - 1)
    correct_answer = str(progression[random_index])
    progression[random_index] = '..'

    task = ' '.join(map(str, progression))
    return correct_answer, task
