from random import choice

available_colors = ["green", "yellow", "red", "blue", "pink", "cyan"]
game_is_on = True


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
    elif color =="red":
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
    u_input = input(f"Please type in a color combination or 'quit' to exit the game.\nPossible colors are {colored_text("green", "green")}, {colored_text("yellow", "yellow")}, {colored_text("red", "red")}, {colored_text("pink", "pink")}, {colored_text("cyan", "cyan")} and {colored_text("blue", "blue")}:\n")
    if u_input == 'quit':
        return u_input
    cleaned_u_input = u_input.split(" ")
    for item in cleaned_u_input:
        if item not in available_colors:
            print(f'Sorry, {item} is not a valid color, please try again.')
            return "invalid"
    if len(cleaned_u_input) != 4:
        print(f'You need to enter exactly 4 colors, but you entered {len(cleaned_u_input)}. Please try again.')
        return "invalid"
    return cleaned_u_input


while game_is_on:
    code_to_guess = generate_code()
    user_input = take_user_input()
    if user_input == 'quit':
        game_is_on = False
    elif user_input != 'invalid':
        print(f'Received user input {user_input} as valid input.')
        print('Moving on to the rest of the program')