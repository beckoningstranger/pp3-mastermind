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
    u_input = input(f'Please type in a color combination. Possible colors are {colored_text("green", "green")}, {colored_text("yellow", "yellow")}, {colored_text("red", "red")}, {colored_text("pink", "pink")}, {colored_text("cyan", "cyan")} and {colored_text("blue", "blue")}: ')
    cleaned_u_input = u_input.split(" ")
    print(type(cleaned_u_input))
    print(f'You typed: {cleaned_u_input}')
    return u_input


while game_is_on:
    code_to_guess = generate_code()
    user_input = take_user_input()
    if user_input == 'quit':
        game_is_on = False