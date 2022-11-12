#!/usr/bin/env python3

from . import core


def generate_progression():
    step = core.get_random_number()
    begin = core.get_random_number()
    length = core.get_random_number(5, 10)
    end = (step * length) + begin

    progression = []
    for num in range(begin, end, step):
        progression.append(str(num))

    return progression


def hide(progression, index):
    progression[index] = '..'


def main():
    name = core.greeting()
    print('What number is missing in the progression?')
    i = 0
    is_win = True

    while i < core.GAMES_COUNT:
        progression = generate_progression()
        hidden_number_index = core.get_random_number(0, len(progression) - 1)
        corrent_answer = progression[hidden_number_index]

        hide(progression, hidden_number_index)
        core.print_question(' '.join(progression))

        answer = core.get_answer()
        is_correct_answer = core.compare_answers(answer, corrent_answer)
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
