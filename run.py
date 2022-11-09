from random import choice
from os import system
from time import sleep
from art import logo, closer, opener


def setup_game():
    global available_colors
    global number_of_allowed_tries
    global game_is_on
    global playing_field
    global round
    global code_to_guess
    available_colors = ["green", "yellow", "red", "blue", "pink", "cyan"]
    number_of_allowed_tries = 8
    game_is_on = True
    playing_field = []
    playing_field = create_playing_field()
    round = 1
    code_to_guess = generate_code()


def create_playing_field():
    playing_field.append(opener)
    for i in range(number_of_allowed_tries, 0, -1):
        playing_field.append(f'│ {i:02d}|--------O--------O---------O--------0--------│------O-O-O-O------ │')
    playing_field.append(closer)
    return playing_field


def add_user_input_to_playing_field(rnd, user_input):
    first_color = user_input[0]
    second_color = user_input[1]
    third_color = user_input[2]
    fourth_color = user_input[3]
    spacer6 = '------'
    spacer8 = '--------'
    spacer9 = '---------'
    round_number = -abs(rnd) + number_of_allowed_tries + 1
    playing_field[round_number] = f"| {rnd:02d}|{spacer8}{formatted_number(first_color)}{spacer8}{formatted_number(second_color)}{spacer9}{formatted_number(third_color)}{spacer8}{formatted_number(fourth_color)}{spacer8}|{spacer6}O-O-O-O{spacer6} |"


def formatted_number(user_input):
    return colored_text("■", user_input)


def print_playing_field():
    system('clear')
    print(logo)
    for line in playing_field:
        print(line)


def generate_code():
    """
    Doc string
    """
    code = []
    for _ in range(4):
        code.append(choice(available_colors))
    return code


def colored_text(text, color):
    if color == "yellow":
        color = '\x1b[93m'
    elif color == "red":
        color = '\x1b[91m'
    elif color == "pink":
        color = '\x1b[95m'
    elif color == "green":
        color = '\x1b[92m'
    elif color == "cyan":
        color = '\x1b[96m'
    elif color == "blue":
        color = '\x1b[94m'
    return color + text + '\x1b[39m'


def take_user_input():
    u_input = input(f"Please type in a color combination or 'quit' to exit the game.\nPossible colors are {colored_text('green', 'green')}, {colored_text('yellow', 'yellow')}, {colored_text('red', 'red')}, {colored_text('pink', 'pink')}, {colored_text('cyan', 'cyan')} and {colored_text('blue', 'blue')}:\nRound {round}: ")
    if u_input == 'quit':
        return u_input
    cleaned_u_input = u_input.split(" ")
    for item in cleaned_u_input:
        if item not in available_colors:
            print(f'Sorry, {item} is not a valid color, please try again.')
            sleep(1)
            return "invalid"
    if len(cleaned_u_input) != 4:
        print(f'You need to enter exactly 4 colors, but you entered {len(cleaned_u_input)}. Please try again.')
        sleep(1)
        return "invalid"
    return cleaned_u_input


def evaluate_user_input(user_guesses, round):
    round_number = -abs(round) + number_of_allowed_tries + 1
    index_counter = 0
    for guess in user_guesses:
        if guess == code_to_guess[index_counter]:
            sleep(1)
            playing_field[round_number] = playing_field[round_number].replace("O", "✓", 1)
        elif guess in code_to_guess:
            sleep(1)
            playing_field[round_number] = playing_field[round_number].replace("O", "◊", 1)
        else:
            sleep(1)
            playing_field[round_number] = playing_field[round_number].replace("O", "X", 1)
        index_counter += 1
        print_playing_field()
        sleep(1)


setup_game()
while game_is_on:
    print_playing_field()
    # print(f'Pssst, the solution is: {code_to_guess}')
    user_input = take_user_input()
    if user_input == 'quit':
        game_is_on = False
    elif user_input != 'invalid':
        print(f'Received user input {user_input} as valid input.')
        add_user_input_to_playing_field(round, user_input)
        print_playing_field()
        evaluate_user_input(user_input, round)
        # Check for win:
        line_to_check = -abs(round) + number_of_allowed_tries + 1
        if "✓-✓-✓-✓" in playing_field[line_to_check]:
            print('You win! Congratulations!')
            game_is_on = False
        round += 1
        # Check for loss:
        if round > 12:
            print('You lose! Better luck next time!')
            game_is_on = False
