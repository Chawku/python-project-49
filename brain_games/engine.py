import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_core(game):
    name = greet()
    print(game.RULES)
    i = 0

    while i < 3:
        correct_answer, task = game.challenge()
        print(f'Question: {task}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            i += 1

        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f"\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
