#!/usr/bin/env python3

from . import core
from math import gcd


def main():
    name = core.greeting()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    is_win = True

    while i < core.GAMES_COUNT:
        first_operand = core.get_random_number()
        second_operand = core.get_random_number()

        correct_answer = gcd(first_operand, second_operand)
        core.print_question(f'{first_operand} {second_operand}')
        answer = core.get_answer()

        is_correct_answer = core.compare_answers(answer, str(correct_answer))
        is_win = is_correct_answer
        if is_correct_answer is not True:
            break
        i += 1

    if is_win:
        core.print_win_game_notification(name)
    else:
        core.print_failed_game_notification(name)


if __name__ == '__main__':
    main()
