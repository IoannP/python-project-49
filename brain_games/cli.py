import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?', True)
    print(f'Hello, {name.strip()}!')
