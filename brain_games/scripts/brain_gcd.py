#!/usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.utils import get_random_number, print_question, get_answer
from math import gcd


def run():
    print('Find the greatest common divisor of given numbers.')

    first_operand = get_random_number()
    second_operand = get_random_number()

    print_question(f'{first_operand} {second_operand}')

    correct_answer = gcd(first_operand, second_operand)
    user_answer = get_answer()

    return user_answer, correct_answer


if __name__ == '__main__':
    rules = 'Find the greatest common divisor of given numbers.'
    run_game(run, rules)
