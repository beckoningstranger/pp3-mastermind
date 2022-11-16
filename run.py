"""
In this game, the computer creates a color code that the player has to guess.
After each guessing round, the computer generates feedback that the player can
use to improve his guess until he gets the color combination or runs out of
tries.
"""
from random import choice
from os import system
from time import sleep
from art import LOGO, CLOSER


AVAILABLE_COLORS = ["green", "yellow", "red", "blue", "pink",
                    "cyan", "white", "black", "blank"]


def create_playing_field(number_of_allowed_tries, code_to_guess):
    """
    Takes how many tries user has and how long the code is, then
    creates a list of strings that makes of the playing field.
    To make the last try appear on top of the list, it steps through
    the range from first to last try in reverse order.
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
    Print out the playing field by having the logo at the top and then
    printing every line of the list that contains the playing field.
    """
    system('clear')
    print(LOGO)
    for line in playing_field:
        print(line)
    print(CLOSER)


def add_user_input_to_playing_field(rnd, user_inp, number_of_allowed_tries):
    """
    Modify the string that holds the information for this turn so that
    the colors the user entered will appear on the playing field.
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
    This allows to output colored text by attaching the codes belows
    in front of the text. The last code resets the color.
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
    Instructs the user about his options and how valid input is formatted.
    Checks if user input is formatted correctly and loops back if it is not.
    """
    u_input = input(f"Enter a color combination (blanks are allowed) or 'quit'"
                    f" to quit this game.\nValid are blank, "
                    f"{colored_text('green', 'green')}, "
                    f"{colored_text('yellow', 'yellow')}, "
                    f"{colored_text('red', 'red')}, "
                    f"{colored_text('pink', 'pink')}, "
                    f"{colored_text('cyan', 'cyan')}, "
                    f"{colored_text('white', 'white')}, "
                    f"{colored_text('black', 'black')} and "
                    f"{colored_text('blue', 'blue')},\n"
                    f"e.g. 'green blank pink cyan' or 'red black white' "
                    f"without the quotation marks:"
                    f"\nRound {turn}: ").lower()
    if u_input == 'quit':
        return u_input
    # This is the cheat code that will reveal the solution if entered
    if u_input == 'iseedeadpeople':
        global cheat_mode
        cheat_mode = True
        return "invalid"
    cleaned_u_input = u_input.split()
    # Check whether all entered items are valid colors
    for item in cleaned_u_input:
        if item not in AVAILABLE_COLORS:
            print_playing_field()
            print(f"Sorry, '{item}' is not a valid color, please try again.")
            sleep(3)
            return "invalid"
    # Check whether the user entered as many colors as there are in the code
    if len(cleaned_u_input) != len(code_to_guess):
        print_playing_field()
        print(f'You need to enter exactly {len(code_to_guess)} '
              f'colors (blanks are also allowed),\n'
              f'but you entered {len(cleaned_u_input)}. '
              f'Please try again.')
        sleep(3)
        return "invalid"
    return cleaned_u_input


def evaluate_user_input(guesses, round_no, allowed_tries, code_to_guess):
    """
    Does what the codemaker would do when it is his turn. Puts key pegs
    on the board for every color the codebreaker has guessed.
    """
    round_number = -abs(round_no) + allowed_tries
    index_counter = 0
    for guess in guesses:
        # Check if color is correct AND in correct place. If so, put a green ✓
        if guess == code_to_guess[index_counter]:
            sleep(1)
            playing_field[round_number] = playing_field[round_number]\
                .replace("O", colored_text("✓", "green"), 1)
        elif guess in code_to_guess:
            # Check if color is anywhere in the code. If so, put a white ◊
            sleep(1)
            playing_field[round_number] = playing_field[round_number]\
                .replace("O", colored_text("◊", "white"), 1)
        else:
            # If neither of the two above, put a red X
            sleep(1)
            playing_field[round_number] = playing_field[round_number]\
                .replace("O", colored_text("X", "red"), 1)
        index_counter += 1
        print_playing_field()
        print('You entered: ', end='')
        for guess in guesses:
            print(f"{colored_text(guess, guess)} ", end='')
        print()
        print(f"Remember: '{colored_text('✓', 'green')}' means you got "
              f"position and color right\n"
              f"          '{colored_text('◊', 'white')}' means while the "
              f"color is in the code, its position is incorrect.\n"
              f"          '{colored_text('X', 'red')}' means this color "
              f"is not in the code")
    input("Press Enter to continue...")


def next_game():
    """
    Asks the user if they would like to play again.
    If user enters anything but "y" or "n", it loops back.
    """
    global keep_playing
    new_game = input('Would you like to play again? (y/n)')
    if new_game == "y":
        system('clear')
        return
    elif new_game == "n":
        print_playing_field()
        print('Thanks for playing! Goodbye!')
        keep_playing = False
        return
    else:
        print_playing_field()
        print("Invalid input, please enter either 'y' or 'n'.")
        next_game()


def explain_the_game():
    """
    This explanation of the game is shown to the user after he starts the game.
    """
    system('clear')
    print(
        f"Welcome to Mastermind!\n\n"
        f"Mastermind was a popular board game in the 70ies and 80ies, where\n"
        f"one player picks 4-5 colors (or blanks) to make up a code that the\n"
        f"other player tries to guess. This is done by entering a color code "
        f"per\n"
        f"round, after every one of which the codemaker gives feedback on "
        f"the\n"
        f"entered code. This feedback gives the codebreaker the information"
        f"they\n"
        f"need to find out the code and win or run out of tries and lose.\n\n"
        f"For each color that the codebreaker gets right _and_ that he also"
        f"put \n"
        f"in the correct spot, the codemaker places a black key peg on the\n"
        f"board. For each color that is not in the correct spot,"
        f"but which is\n"
        f"in the code at another position, the codemaker places a white\n"
        f"key peg.\n\n"
        f"In this game, the key pegs are replaced by green checkmarks "
        f"({colored_text('✓', 'green')})\n"
        f"and white rhombi "
        f"({colored_text('◊', 'white')}), and of course the codemaker is "
        f"played entirely by\n"
        f"the computer. Also, you can pick how long the color code should be\n"
        f"and how many tries you have before you lose, but otherwise the "
        f"rules\n"
        f"are the same. Duplicate colors are allowed and the code may also\n"
        f"include blanks. Theoretically, it's even possible that the code is\n"
        f"entirely made up of blanks.\n")
    input("Enjoy playing! Press Enter to continue...")
    system('clear')


def gather_game_params():
    """
    Here, the users sets how long the colors code will be and how many tries
    he has to guess the code.
    """
    print(LOGO)
    number_of_allowed_tries = 0
    try:
        code_length = int(input("How long do you want the color code "
                                "to be? (3-7) "))
        # try will catch input that's a string or multiple numbers, but not
        # numbers that are outside the specified range. This if-statement will.
        if code_length <= 2 or code_length >= 8:
            code_length = "error"
    except (TypeError, ValueError):
        code_length = "error"
    if code_length != "error":
        try:
            number_of_allowed_tries = int(input("How many tries are allowed "
                                                "before you lose? (4-10) "))
            if number_of_allowed_tries <= 3 or number_of_allowed_tries >= 11:
                number_of_allowed_tries = "error"
        except (TypeError, ValueError):
            number_of_allowed_tries = "error"
    return code_length, number_of_allowed_tries


def play_game(code_length, number_of_allowed_tries):
    """
    This takes how long the code is and how many tries the user has
    before he loses and then manages the whole game.
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
        # If cheat mode is active, this will print the solution
        if cheat_mode:
            print('Pssst, the solution is: ', end='')
            for i in code_to_guess:
                print(colored_text(i, i), end=' ')
            print()
        # Allow users to enter their guess or quit the game
        user_input = take_user_input(current_turn, code_to_guess)
        if user_input == 'quit':
            print_playing_field()
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
                print('You have run out of tries and lose! Better luck '
                      'next time!')
                print('The solution was:', end=' ')
                for i in code_to_guess:
                    print(colored_text(i, i), end=' ')
                print()
                game_is_on = False
    next_game()


def main():
    """
    This first explains the game, then asks for game parameters, then starts
    the game after which it will ask whether the user wants to play again.
    If so, it loops around.
    """
    global keep_playing
    keep_playing = True
    explain_the_game()
    while keep_playing:
        game_parameters = gather_game_params()
        given_code_length = game_parameters[0]
        given_amount_of_tries = game_parameters[1]
        if given_amount_of_tries != "error" and given_code_length != "error":
            play_game(given_code_length, given_amount_of_tries)
        else:
            print('Invalid input, please try again!')
            sleep(2)
            system('clear')


main()
