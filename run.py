from random import choice
from os import system
from time import sleep
from art import logo, closer, opener


def create_playing_field(number_of_allowed_tries):
    playing_field.append(opener)
    for i in range(number_of_allowed_tries, 0, -1):
        playing_field.append(f'│ {i:02d}|--------O--------O---------O--------0--------│------O-O-O-O------ │')
    playing_field.append(closer)
    return playing_field


def add_user_input_to_playing_field(rnd, user_inp, number_of_allowed_tries):
    first_color = user_inp[0]
    second_color = user_inp[1]
    third_color = user_inp[2]
    fourth_color = user_inp[3]
    spacer6 = '------'
    spacer8 = '--------'
    spacer9 = '---------'
    round_number = -abs(rnd) + number_of_allowed_tries + 1
    playing_field[round_number] = f"| {rnd:02d}|{spacer8}{formatted_number(first_color)}{spacer8}" \
                                  f"{formatted_number(second_color)}{spacer9}{formatted_number(third_color)}{spacer8}" \
                                  f"{formatted_number(fourth_color)}{spacer8}|{spacer6}O-O-O-O{spacer6} |"


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


def generate_code(available_colors):
    """
    Doc string
    """
    code = []
    for _ in range(4):
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


def take_user_input(available_colors, turn):
    u_input = input(f"Enter a color combination (blanks are allowed) or 'quit' to stop playing.\n"
                    f"Valid are 'blank', {colored_text('green', 'green')}, "
                    f"{colored_text('yellow', 'yellow')}, {colored_text('red', 'red')}, {colored_text('pink', 'pink')},"
                    f" {colored_text('cyan', 'cyan')}, {colored_text('white', 'white')}, "
                    f"{colored_text('black', 'black')} and {colored_text('blue', 'blue')},\ne.g. 'green red pink cyan':"
                    f"\nRound {turn}: ")
    if u_input == 'quit':
        return u_input
    cleaned_u_input = u_input.split(" ")
    for item in cleaned_u_input:
        if item not in available_colors:
            print(f'Sorry, {item} is not a valid color, please try again.')
            sleep(1)
            return "invalid"
    if len(cleaned_u_input) != 4:
        print(f'You need to enter exactly 4 colors (blanks are also allowed), but you entered {len(cleaned_u_input)}. '
              f'Please try again.')
        sleep(1)
        return "invalid"
    return cleaned_u_input


def evaluate_user_input(user_guesses, round_no, number_of_allowed_tries, code_to_guess):
    round_number = -abs(round_no) + number_of_allowed_tries + 1
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
        print(f"Slowly evaluating your input for dramatic effect...\nRemember:\n'✓' means you got position and "
              f"color right\n'◊' means the color is in the code, but it's not in the correct position\n'X' "
              f"means this color is not in the code")
        sleep(1)


def main():
    available_colors = ["green", "yellow", "red", "blue", "pink", "cyan", "white", "black", "blank"]
    number_of_allowed_tries = 8
    playing_field = create_playing_field(number_of_allowed_tries)
    turn = 1
    code_to_guess = generate_code(available_colors)
    game_is_on = True
    while game_is_on:
        print_playing_field()
        # print(f'Pssst, the solution is: {code_to_guess}')
        user_input = take_user_input(available_colors, turn)
        if user_input == 'quit':
            game_is_on = False
        elif user_input != 'invalid':
            add_user_input_to_playing_field(turn, user_input, number_of_allowed_tries)
            print_playing_field()
            evaluate_user_input(user_input, turn, number_of_allowed_tries, code_to_guess)
            # Check for win:
            line_to_check = -abs(turn) + number_of_allowed_tries + 1
            if "✓-✓-✓-✓" in playing_field[line_to_check]:
                print('You win! Congratulations!')
                game_is_on = False
            turn += 1
            # Check for loss:
            if turn > 12:
                print('You lose! Better luck next time!')
                game_is_on = False


playing_field = []
main()
