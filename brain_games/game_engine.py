import prompt


ROUNDS = 3


def play_game(run_game, game_rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    is_won = True
    i = ROUNDS

    print(game_rules)

    while i:
        question, correct_answer = run_game()

        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')

        if player_answer == str(correct_answer):
            print('Correct!')
        else:
            print(f'\'{player_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            is_won = False
            break
        i -= 1

    if is_won:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')
