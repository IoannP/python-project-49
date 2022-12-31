import prompt


GAMES_COUNT = 3


def run_game(run, game_rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    is_won = True
    i = GAMES_COUNT

    print(game_rules)

    while i:
        user_answer, correct_answer = run()
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            is_won = False
            break
        i -= 1

    if is_won:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')
