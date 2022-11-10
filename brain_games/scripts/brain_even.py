#!/usr/bin/env python3

import prompt
import random


def get_random_number(begin=1, end=100):
    return random.randint(begin, end)


def is_even(num):
    return num % 2 == 0


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.strip()}!')
    print('Answer "yes" if the number is even, otherwise answer "no"')

    game_count = 3
    i = 0
    while i < game_count:
        number = get_random_number()

        correct_answer = 'yes' if is_even(number) else 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if correct_answer == answer.strip():
            print('Correct!')
        else:
            print(f'\'{answer.strip()}\' is wrong onswer ;(.'
                  f'Correct answer was \'{correct_answer}\'.')
            print('Let\'s try again, Bill!')
            return False
        i += 1
    print('Congratulations, Bill!')
    return True


if __name__ == '__main__':
    main()
