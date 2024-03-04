#!/usr/bin/env python3

import prompt
import random


user_name = prompt.string('May I have your name? ')
print("Hello, " + user_name + '!')
print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    random_num = random.randint(1, 100)
    print('Question: ' + str(random_num))
    user_answer = input()

    while True:
        correct_answer = 'yes' if random_num % 2 == 0 else 'no'

        if user_answer.lower() == correct_answer:
            print('Correct!')
            return
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            return main()


if __name__ == '__main__':
    main()


main()
main()
