
string = 'geometry is very very cool'


def cipher(phrase: str):
    final = ''
    counter = 0
    count = 0
    for this_char in phrase:
        if this_char != ' ':
            row_numbers = str(11 ** counter)
            this_char = chr((((ord(this_char) - 97) + 1 + int(row_numbers[count])) % 26) + 97)
            if count + 1 == len(row_numbers):
                count = 0
                counter += 1
            else:
                count += 1

        final += this_char
    return final




print(cipher(string))