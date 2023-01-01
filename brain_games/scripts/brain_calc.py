#!/usr/bin/env python3

from operator import add, mul, sub
from brain_games.game_engine import play_game
from brain_games.utils import get_random_number


def get_operator():
    num = get_random_number(1, 3)
    if num == 1:
        return '*'
    elif num == 2:
        return '-'
    else:
        return '+'


def calculate(operator, first_operand, second_operand):
    if operator == '*':
        return mul(first_operand, second_operand)
    if operator == '-':
        return sub(first_operand, second_operand)
    if operator == '+':
        return add(first_operand, second_operand)


def run_calc_game():
    first_operand = get_random_number()
    second_operand = get_random_number()
    operator = get_operator()

    question = f'{first_operand} {operator} {second_operand}'
    correct_answer = calculate(operator, first_operand, second_operand)

    return question, correct_answer


def main():
    rules = 'What is the result of the expression?'
    play_game(run_calc_game, rules)


if __name__ == '__main__':
    main()
