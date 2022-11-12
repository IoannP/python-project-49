#!/usr/bin/env python3

from . import core


def is_prime(number):
    if number == 1:
        return False

    for n in range(2, number // 2):
        if number % n == 0:
            return False

    return True


def main():
    name = core.greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    is_win = True

    while i < core.GAMES_COUNT:
        number = core.get_random_number()
        correct_answer = 'yes' if is_prime(number) else 'no'

        core.print_question(number)
        answer = core.get_answer()
        is_correct_answer = core.compare_answers(answer, correct_answer)

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
