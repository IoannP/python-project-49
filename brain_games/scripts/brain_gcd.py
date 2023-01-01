#!/usr/bin/env python3

from brain_games.game_engine import play_game
from brain_games.utils import get_random_number
from math import gcd


def run_gcd_game():
    first_operand = get_random_number()
    second_operand = get_random_number()

    question = f'{first_operand} {second_operand}'
    correct_answer = gcd(first_operand, second_operand)

    return question, correct_answer


def main():
    rules = 'Find the greatest common divisor of given numbers.'
    play_game(run_gcd_game, rules)


if __name__ == '__main__':
    main()
