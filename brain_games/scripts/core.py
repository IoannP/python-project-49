import prompt
import random


GAMES_COUNT = 3


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def print_question(question):
    print(f'Question: {question}')


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def compare_answers(answer, correct_answer):
    is_correct = answer == correct_answer
    if is_correct:
        print('Correct!')
    else:
        print(f'\'{answer}\' is wrong answer ;(. '
              f'Correct answer was \'{correct_answer}\'.')
    return is_correct


def get_random_number(min=1, max=100):
    return random.randint(min, max)


def print_win_game_notification(name):
    print(f'Congratulations, {name}!')


def print_failed_game_notification(name):
    print(f'Let\'s try again, {name}!')
