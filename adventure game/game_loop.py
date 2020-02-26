from os import _exit, system
from time import sleep
from functions import create_options, load_json, print_choices
from char_tools import classnames, Character
from scenario import start_scenario


def loadsave(DEBUG):
    choices = list(load_json("saves/characters.JSON").keys())
    choice_list = create_options(choices)
    character_name = choices[int(input(f'Select your character name from the following\n{choice_list}\n')) - 1]
    this_char = Character()
    this_char.load(character_name)
    system('cls')
    print(f'{this_char.name} loaded, your adventure continues...')
    sleep(2)
    system('cls')
    return this_char


def newgame(DEBUG):

    char_name = input("Type a character name and press Enter\n")
    name_exist_check = load_json('saves/characters.JSON')
    if char_name in list(name_exist_check.keys()):
        confirm_overwrite = input(f'This will delete your existing character named {char_name}, would you like to continue anyway\ny/n?').lower()
        if 'n' in confirm_overwrite:
            return start(DEBUG)
    class_role_options = list(classnames.keys())
    options = '\n'.join([f'[{count + 1}]: ' + x for count, x in enumerate(class_role_options)])
    char_class = class_role_options[int(input(f'Chose one of the following classes:\n{options}\n')) -1]
    char_object = Character(char_name, char_class)
    char_object.save()
    system('cls')
    print(f'New Character {char_object.name} created. Your adventure begins...')
    sleep(2)
    system('cls')
    return char_object

def start(DEBUG):

    system('color 02')
    menu_options = ['new game', 'load game']
    first = print_choices("Hello and welcome to Adventure Game!", menu_options)

    system('cls')

    if first == 'new game':
        player = newgame(DEBUG)

    elif first == 'load game':
        player = loadsave(DEBUG)


    return start_scenario(player)