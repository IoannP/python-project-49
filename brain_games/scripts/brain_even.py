#!/usr/bin/env python3

from brain_games.game_engine import play_game
from brain_games.utils import get_random_number


def is_even(num):
    return num % 2 == 0


def run_even_game():
    question = get_random_number()
    correct_answer = 'yes' if is_even(question) else 'no'

    return question, correct_answer


def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_game(run_even_game, rules)


if __name__ == '__main__':
    main()
