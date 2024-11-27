import prompt

ROUNDS_COUNT = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    print(game.RULES, "\n")

    for _ in range(ROUNDS_COUNT):
        correct_answer, task = game.generate_question()
        print(f'Question: {task}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!\n')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
