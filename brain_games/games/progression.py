import random

RULES = 'What number is missing in the progression?'


def progression():
    task = []
    initial_number, difference = random.randint(1, 30), random.randint(1, 30)
    length = 10
    for i in range(length):
        initial_number += difference
        task.append(initial_number)

    random_index = random.randint(0, 9)
    correct_answer = str(task[random_index])
    return task, correct_answer, random_index


def challenge():
    task, correct_answer, random_index = progression()
    task[random_index] = '..'
    task = ' '.join(str(i) for i in task)
    return correct_answer, task
