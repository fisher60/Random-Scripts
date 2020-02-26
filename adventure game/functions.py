import json
from os import system as sys
from os import _exit

def save_json(file: str, content: dict, key=None):

    with open(file, "r") as f:
        this_file = json.load(f)

    if key is None:
        index = list(content.keys())[0]
        this_file[index] = content[index]

    else:
        this_file[key] = content

    with open(file, "w") as f:
        json.dump(this_file, f)


def load_json(file: str, key=None):
    with open(file, "r") as f:
        if key is None:
            return json.load(f)
        else:
            return json.load(f)[key]


def create_options(options: list):
    return '\n'.join([f'[{count + 1}]: ' + x for count, x in enumerate(options)])

def print_choices(text: str, options: list):
    options.append("Exit game")
    text_options = create_options(options)
    choice = options[int(input(f'{text}\n{text_options}\n')) - 1]
    if choice == "Exit game":
        clear()
        print("Bye, thank you for playing!")
        choice = _exit(2)
    return choice

def clear():
    return sys('cls')