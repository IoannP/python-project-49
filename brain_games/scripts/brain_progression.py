#!/usr/bin/env python3

from brain_games.game_engine import play_game
from brain_games.utils import get_random_number


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


def run_progression_game():
    progression = generate_progression()
    hidden_number_index = get_random_number(0, len(progression) - 1)

    corrent_answer = progression[hidden_number_index]
    hide(progression, hidden_number_index)

    return ' '.join(progression), corrent_answer


def main():
    rules = 'What number is missing in the progression?'
    play_game(run_progression_game, rules)


if __name__ == '__main__':
    main()
