#!/usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.utils import get_random_number, print_question, get_answer


def get_operator():
    num = get_random_number(1, 3)
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


def run(game_count):
    print('What is the result of the expression?')

    while game_count:
        first_operand = get_random_number()
        second_operand = get_random_number()
        operator = get_operator()

        print_question(f'{first_operand} {operator} {second_operand}')

        correct_answer = calculate_answer(operator,
                                          first_operand,
                                          second_operand)
        user_answer = get_answer()

        return user_answer, correct_answer


if __name__ == '__main__':
    rules = 'What is the result of the expression?'
    run_game(run, rules)
