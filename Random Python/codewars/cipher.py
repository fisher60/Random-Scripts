import random

string = 'if you made it this far you are a better programmer than i am'

characters = [chr(x) for x in range(97, 123)]

for item in range(8):
    characters.append(' ')


def random_gen_alpha ():
    return ''.join([random.choice(characters) for y in range(random.randint(0, 30))])


def alpha_reverse(string: str):
    final = ''
    for x in string:
        if x == ' ':
            final += x
        else:
            this_ord = 123 - ord(x)
            conv_to_reverse = this_ord + 96
            final += chr(conv_to_reverse)

    return final


def second_cipher(phrase):
    final = ''
    row = 0
    for count, char in enumerate(phrase):
        col = count % 3
        if char != ' ':
            final += chr(((ord(char) - 97) + (row + col)) % 26 + 97)
        else:
            final += char
        if not col and count > 0:
            row += 1
    return final


def reverse_second_cipher(phrase):
    final = ''
    row = 0
    for count, char in enumerate(phrase):
        col = count % 3
        if char != ' ':
            final += chr(((ord(char) - 97) - (row + col)) % 26 + 97)
        else:
            final += char
        if not col and count > 0:
            row += 1
    return final

print(f'Refactor: {second_cipher(string)}')
print(f'Refactor: {reverse_second_cipher(second_cipher(string))}')



