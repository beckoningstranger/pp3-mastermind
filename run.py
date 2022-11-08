from random import choice


def generate_code():
    """
    Doc string
    """
    available_colors = ["green", "yellow", "red", "blue", "teal", "pink", "orange", "cyan"]
    code = []
    for _ in range(5):
        code.append(choice(available_colors))
    return code


code = generate_code()
print(code)