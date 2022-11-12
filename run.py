"""
Placeholder Doc String
"""
from random import choice
from os import system
from time import sleep
from art import LOGO, CLOSER


AVAILABLE_COLORS = ["green", "yellow", "red", "blue", "pink",
                    "cyan", "white", "black", "blank"]


def create_playing_field(number_of_allowed_tries, code_to_guess):
    """
    Placeholder Doc String
    """
    p_f = []
    for i in range(number_of_allowed_tries, 0, -1):
        if len(code_to_guess) == 3:
            p_f.append(f'│ {i:02d}|-----------O----------O----------O---------'
                       f'--│-------O-O-O------- │')
        elif len(code_to_guess) == 4:
            p_f.append(f'│ {i:02d}|--------O--------O---------O--------O------'
                       f'--│------O-O-O-O------ │')
        elif len(code_to_guess) == 5:
            p_f.append(f'│ {i:02d}|------O-------O-------O-------O-------O----'
                       f'--│-----O-O-O-O-O----- │')
        elif len(code_to_guess) == 6:
            p_f.append(f'│ {i:02d}|-----O------O------O------O------O-----O---'
                       f'--│----O-O-O-O-O-O---- │')
        elif len(code_to_guess) == 7:
            p_f.append(f'│ {i:02d}|----O-----O-----O-----O-----O-----O-----O--'
                       f'--│---O-O-O-O-O-O-O--- │')
    return p_f


def print_playing_field():
    """
    Placeholder Doc String
    """
    system('clear')
    print(LOGO)
    for line in playing_field:
        print(line)
    print(CLOSER)


def add_user_input_to_playing_field(rnd, user_inp, number_of_allowed_tries):
    """
    Placeholder Doc String
    """
    round_number = -abs(rnd) + number_of_allowed_tries
    previous_rnd_number = f'{round_number -1}:02d'
    playing_field[round_number] = playing_field[round_number].replace(
        previous_rnd_number, f'{round_number}:02d', 1)
    for color in user_inp:
        if color == "blank":
            playing_field[round_number] = playing_field[round_number]\
                .replace("O", " ", 1)
        else:
            playing_field[round_number] = \
                playing_field[round_number]\
                .replace("O", colored_text("■", color), 1)


def generate_code(code_length):
    """
    Creates a code from the available colors.
    The length of the code depends on variable code_length.
    """
    code = []
    for _ in range(code_length):
        code.append(choice(AVAILABLE_COLORS))
    return code


def colored_text(text, color):
    """
    Placeholder Doc String
    """
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
    elif color == "blank":
        color = '\x1b[39m'
    elif color == "black":
        color = '\x1b[90m'
    elif color == "white":
        color = '\x1b[97m'
    return color + text + '\x1b[39m'


def take_user_input(turn, code_to_guess):
    """
    Placeholder Doc String
    """
    u_input = input(f"Enter a color combination (blanks are allowed) or 'quit'"
                    f" to stop this game.\nValid are 'blank', "
                    f"{colored_text('green', 'green')}, "
                    f"{colored_text('yellow', 'yellow')}, "
                    f"{colored_text('red', 'red')}, "
                    f"{colored_text('pink', 'pink')}, "
                    f"{colored_text('cyan', 'cyan')}, "
                    f"{colored_text('white', 'white')}, "
                    f"{colored_text('black', 'black')} and "
                    f"{colored_text('blue', 'blue')},\n"
                    f"e.g. 'green red pink cyan':"
                    f"\nRound {turn}: ").lower()
    if u_input == 'quit':
        return u_input
    if u_input == 'iseedeadpeople':
        global cheat_mode
        cheat_mode = True
        return "invalid"
    cleaned_u_input = u_input.split(" ")
    for item in cleaned_u_input:
        if item not in AVAILABLE_COLORS:
            print(f'Sorry, {item} is not a valid color, please try again.')
            sleep(3)
            return "invalid"
    if len(cleaned_u_input) != len(code_to_guess):
        print(f'You need to enter exactly {len(code_to_guess)} '
              f'colors (blanks are also allowed), '
              f'but you entered {len(cleaned_u_input)}. '
              f'Please try again.')
        sleep(3)
        return "invalid"
    return cleaned_u_input


def evaluate_user_input(guesses, round_no, allowed_tries, code_to_guess):
    """
    Placeholder Doc String
    """
    round_number = -abs(round_no) + allowed_tries
    index_counter = 0
    for guess in guesses:
        if guess == code_to_guess[index_counter]:
            sleep(1)
            playing_field[round_number] = playing_field[round_number]\
                .replace("O", colored_text("✓", "green"), 1)
        elif guess in code_to_guess:
            sleep(1)
            playing_field[round_number] = playing_field[round_number]\
                .replace("O", colored_text("◊", "white"), 1)
        else:
            sleep(1)
            playing_field[round_number] = playing_field[round_number]\
                .replace("O", colored_text("X", "red"), 1)
        index_counter += 1
        print_playing_field()
        print("Remember: '✓' means you got position and color right\n"
              "          '◊' means the color is in the code, the position is"
              " incorrect.\n"
              "          'X' means this color is not in the code")
    input("Press Enter to continue...")


def next_game():
    """
    Placeholder Doc String
    """
    global keep_playing
    new_game = input('Would you like to play again? (y/n)')
    if new_game == "y":
        return
    elif new_game == "n":
        print_playing_field()
        print('Thanks for playing! Goodbye!')
        keep_playing = False
        return
    else:
        next_game()


def explain_the_game():
    """
    Placeholder Doc String
    """
    system('clear')
    print(LOGO)
    print("I'll add more details here, later.")
    input("Press Enter to continue...")


def gather_game_params():
    """
    Placeholder Doc String
    """
    system('clear')
    print(LOGO)
    code_length = int(input("How long do you want the color"
                            " code to be? (3-7) "))
    number_of_allowed_tries = int(input("How many tries are allowed before "
                                        "you lose? (4-12) "))
    return code_length, number_of_allowed_tries


def start_game(code_length, number_of_allowed_tries):
    """
    Placeholder Doc String
    """
    global cheat_mode
    cheat_mode = False
    current_turn = 1
    code_to_guess = generate_code(code_length)
    global playing_field
    playing_field = create_playing_field(number_of_allowed_tries,
                                         code_to_guess)
    game_is_on = True
    while game_is_on:
        print_playing_field()
        if cheat_mode:
            print('Pssst, the solution is: ', end='')
            for i in code_to_guess:
                print(colored_text(i, i), end=' ')
            print()
        # Allow users to enter their guess or quit the game
        user_input = take_user_input(current_turn, code_to_guess)
        if user_input == 'quit':
            game_is_on = False
        # If user input is not 'quit' and valid, display it on the playing
        # field and evaluate it
        elif user_input != 'invalid':
            add_user_input_to_playing_field(current_turn,
                                            user_input,
                                            number_of_allowed_tries)
            print_playing_field()
            evaluate_user_input(user_input, current_turn,
                                number_of_allowed_tries, code_to_guess)
            # Check for win:
            line_to_check = -abs(current_turn) + number_of_allowed_tries
            # Check whether the current evaluation line contains the required
            # amount of checkmarks:
            if playing_field[line_to_check]\
                    .count(f'{colored_text("✓", "green")}') == \
                    len(code_to_guess):
                print_playing_field()
                print('You win! Congratulations!')
                game_is_on = False
            else:
                current_turn += 1
            # Check for loss:
            if current_turn > number_of_allowed_tries:
                print_playing_field()
                print('You have exhausted your maximum number of tries '
                      'and lose! Better luck next time!')
                print('The solution was:', end=' ')
                for i in code_to_guess:
                    print(colored_text(i, i), end=' ')
                print('')
                game_is_on = False
    next_game()


def main():
    """
    Placeholder Doc String
    """
    global keep_playing
    keep_playing = True
    explain_the_game()
    while keep_playing:
        game_parameters = gather_game_params()
        given_code_length = game_parameters[0]
        given_amount_of_tries = game_parameters[1]
        if given_code_length in range(3, 8) and \
                given_amount_of_tries in range(4, 13):
            start_game(given_code_length, given_amount_of_tries)
        else:
            print('The given game parameters are not within legal limits! '
                  'Please try again.')
            sleep(2)


main()
