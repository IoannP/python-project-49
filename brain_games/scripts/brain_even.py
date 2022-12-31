#!/usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.utils import get_random_number, print_question, get_answer


def is_even(num):
    return num % 2 == 0


def run():
    number = get_random_number()
    print_question(number)

    correct_answer = 'yes' if is_even(number) else 'no'
    user_answer = get_answer()

    return user_answer, correct_answer


if __name__ == '__main__':
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(run, rules)
