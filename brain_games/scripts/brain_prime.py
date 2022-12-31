#!/usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.utils import get_random_number, print_question, get_answer


def is_prime(number):
    if number == 1:
        return False

    for n in range(2, number // 2):
        if number % n == 0:
            return False

    return True


def run():
    number = get_random_number()
    print_question(number)

    correct_answer = 'yes' if is_prime(number) else 'no'
    user_answer = get_answer()

    return user_answer, correct_answer


if __name__ == '__main__':
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(run, rules)
