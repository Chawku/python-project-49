from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def challenge():
    random_num = randint(1, 100)
    flag = is_even(random_num)
    if flag is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, random_num


def is_even(random_num):
    return True if random_num % 2 == 0 else False
