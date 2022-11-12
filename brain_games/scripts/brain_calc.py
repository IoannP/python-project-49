#!/usr/bin/env python3

from . import core


def get_operand():
    num = core.get_random_number(1, 3)
    if num == 1:
        return '*'
    elif num == 2:
        return '-'
    else:
        return '+'


def calculate_answer(operator, first_operand, second_operand):
    if operator == '*':
        return first_operand * second_operand
    if operator == '-':
        return first_operand - second_operand
    if operator == '+':
        return first_operand + second_operand


def main():
    name = core.greeting()
    print('What is the result of the expression?')
    i = 0
    is_win = True

    while i < core.GAMES_COUNT:
        first_operand = core.get_random_number()
        second_operand = core.get_random_number()
        operator = get_operand()

        currect_answer = calculate_answer(operator,
                                          first_operand,
                                          second_operand)

        core.print_question(f'{first_operand} {operator} {second_operand}')
        answer = core.get_answer()

        is_correct_answer = core.compare_answers(answer, str(currect_answer))
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
