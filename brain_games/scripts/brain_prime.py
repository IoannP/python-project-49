#!/usr/bin/env python3

from brain_games.game_engine import play_game
from brain_games.utils import get_random_number


def is_prime(number):
    if number == 1:
        return False

    for n in range(2, number // 2):
        if number % n == 0:
            return False

    return True


def run_prime_game():
    question = get_random_number()
    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer


def main():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play_game(run_prime_game, rules)


if __name__ == '__main__':
    main()
