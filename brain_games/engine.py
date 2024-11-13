import prompt


def game_core(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.RULES)

    for _ in range(3):
        correct_answer, task = game.generate_question()
        print(f'Question: {task}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f"\nLet's try again, {name}!")
            return

    else:
        print(f'Congratulations, {name}!')
