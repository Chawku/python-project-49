import random

RULES = 'What is the result of the expression?'


def generate_question():
    first = random.randint(0, 50)
    second = random.randint(0, 50)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    question = f"{first} {operator} {second}"
    answer = 0

    if operator == '+':
        answer = first + second
    elif operator == "-":
        answer = first - second
    elif operator == "*":
        answer = first * second
    correct_answer = str(answer)
    return correct_answer, question
