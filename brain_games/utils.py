import random
import prompt


def get_random_number(min=1, max=100):
    return random.randint(min, max)


def print_question(question):
    print(f'Question: {question}')


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer
