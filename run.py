from random import choice
from os import system
from time import sleep
from art import logo, closer, opener


def create_playing_field(number_of_allowed_tries, code_to_guess):
    playing_field.append(opener)
    for i in range(number_of_allowed_tries, 0, -1):
        if len(code_to_guess) == 3:
            playing_field.append(f'│ {i:02d}|-----------O----------O----------O-----------│-------O-O-O------- │')
        elif len(code_to_guess) == 4:
            playing_field.append(f'│ {i:02d}|--------O--------O---------O--------O--------│------O-O-O-O------ │')
        elif len(code_to_guess) == 5:
            playing_field.append(f'│ {i:02d}|------O-------O-------O-------O-------O------│-----O-O-O-O-O----- │')
        elif len(code_to_guess) == 6:
            playing_field.append(f'│ {i:02d}|-----O------O------O------O------O-----O-----│----O-O-O-O-O-O---- │')
        elif len(code_to_guess) == 7:
            playing_field.append(f'│ {i:02d}|----O-----O-----O-----O-----O-----O-----O----│---O-O-O-O-O-O-O--- │')
    playing_field.append(closer)
    return playing_field


def add_user_input_to_playing_field(rnd, user_inp, number_of_allowed_tries):
    round_number = -abs(rnd) + number_of_allowed_tries + 1
    previous_rnd_number = f'{round_number -1}:02d'
    playing_field[round_number] = playing_field[round_number].replace(previous_rnd_number, f'{round_number}:02d', 1)
    for i in user_inp:
        playing_field[round_number] = playing_field[round_number].replace("O", formatted_number(i), 1)


def formatted_number(color):
    if color == "blank":
        return colored_text(" ", color)
    else:
        return colored_text("■", color)


def print_playing_field():
    system('clear')
    print(logo)
    for line in playing_field:
        print(line)


def generate_code(available_colors, code_length):
    """
    Doc string
    """
    code = []
    for _ in range(code_length):
        code.append(choice(available_colors))
    return code


def colored_text(text, color):
    match color:
        case "yellow":
            color = '\x1b[93m'
        case "red":
            color = '\x1b[91m'
        case "pink":
            color = '\x1b[95m'
        case "green":
            color = '\x1b[92m'
        case "cyan":
            color = '\x1b[96m'
        case "blue":
            color = '\x1b[94m'
        case "blank":
            color = '\x1b[39m'
        case "black":
            color = '\x1b[90m'
        case "white":
            color = '\x1b[97m'
    return color + text + '\x1b[39m'


def take_user_input(available_colors, turn, code_to_guess):
    u_input = input(f"Enter a color combination (blanks are allowed) or 'quit' to stop playing.\n"
                    f"Valid are 'blank', {colored_text('green', 'green')}, "
                    f"{colored_text('yellow', 'yellow')}, {colored_text('red', 'red')}, {colored_text('pink', 'pink')},"
                    f" {colored_text('cyan', 'cyan')}, {colored_text('white', 'white')}, "
                    f"{colored_text('black', 'black')} and {colored_text('blue', 'blue')},\ne.g. 'green red pink cyan':"
                    f"\nRound {turn}: ").lower()
    if u_input == 'quit':
        return u_input
    if u_input == 'icanseedeadpeople':
        global cheat_mode
        cheat_mode = True
        return "invalid"
    cleaned_u_input = u_input.split(" ")
    for item in cleaned_u_input:
        if item not in available_colors:
            print(f'Sorry, {item} is not a valid color, please try again.')
            sleep(3)
            return "invalid"
    if len(cleaned_u_input) != len(code_to_guess):
        print(f'You need to enter exactly {len(code_to_guess)} colors (blanks are also allowed), '
              f'but you entered {len(cleaned_u_input)}. '
              f'Please try again.')
        sleep(3)
        return "invalid"
    return cleaned_u_input


def evaluate_user_input(user_guesses, round_no, number_of_allowed_tries, code_to_guess):
    round_number = -abs(round_no) + number_of_allowed_tries + 1
    index_counter = 0
    for guess in user_guesses:
        if guess == code_to_guess[index_counter]:
            sleep(1)
            playing_field[round_number] = playing_field[round_number].replace("O", colored_text("✓", "green"), 1)
        elif guess in code_to_guess:
            sleep(1)
            playing_field[round_number] = playing_field[round_number].replace("O", colored_text("◊", "white"), 1)
        else:
            sleep(1)
            playing_field[round_number] = playing_field[round_number].replace("O", colored_text("X", "red"), 1)
        index_counter += 1
        print_playing_field()
        print(f"Slowly evaluating your input for dramatic effect...\nRemember:\n'✓' means you got position and "
              f"color right\n'◊' means the color is in the code, but it's not in the correct position\n'X' "
              f"means this color is not in the code")
        sleep(1)


def main():
    global cheat_mode
    global playing_field
    available_colors = ["green", "yellow", "red", "blue", "pink", "cyan", "white", "black", "blank"]
    cheat_mode = False
    number_of_allowed_tries = 8
    code_length = 7
    turn = 1
    code_to_guess = generate_code(available_colors, code_length)
    playing_field = create_playing_field(number_of_allowed_tries, code_to_guess)
    game_is_on = True
    while game_is_on:
        print_playing_field()
        if cheat_mode:
            print(f'Pssst, the solution is: {code_to_guess}')
        user_input = take_user_input(available_colors, turn, code_to_guess)
        if user_input == 'quit':
            game_is_on = False
        elif user_input != 'invalid':
            add_user_input_to_playing_field(turn, user_input, number_of_allowed_tries)
            print_playing_field()
            evaluate_user_input(user_input, turn, number_of_allowed_tries, code_to_guess)
            # Check for win:
            line_to_check = -abs(turn) + number_of_allowed_tries + 1
            # Check whether the current evaluation line contains the required amount of checkmarks:
            if playing_field[line_to_check].count(f'{colored_text("✓", "green")}') == len(code_to_guess):
                print('You win! Congratulations!')
                game_is_on = False
            turn += 1
            # Check for loss:
            if turn > 12:
                print('You lose! Better luck next time!')
                game_is_on = False


cheat_mode = None
playing_field = []
main()
