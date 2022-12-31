#!/usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.utils import get_random_number, print_question, get_answer


def generate_progression():
    step = get_random_number()
    begin = get_random_number()
    length = get_random_number(5, 10)
    end = (step * length) + begin

    progression = []
    for num in range(begin, end, step):
        progression.append(str(num))

    return progression


def hide(progression, index):
    progression[index] = '..'


def run():
    progression = generate_progression()
    hidden_number_index = get_random_number(0, len(progression) - 1)

    corrent_answer = progression[hidden_number_index]
    user_answer = get_answer()

    hide(progression, hidden_number_index)
    print_question(' '.join(progression))

    return corrent_answer, user_answer


if __name__ == '__main__':
    rules = 'What number is missing in the progression?'
    run_game(run, rules)
