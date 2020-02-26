

string = 'this phrase is 14'
def cipher(phrase: str):
    final = ''
    counter = 0
    for count, this_char in enumerate(phrase):
        # print(count)
        row_position = 0
        if this_char != ' ':
            row_numbers = str(11 ** counter)
            if count > 0:
                row_position = (int(row_numbers[1])+1) % count
                if row_position == 0:
                    counter += 1
            else:
                counter += 1
            this_char = chr(((ord(this_char) - 97) + int(row_numbers[row_position]) % 26) + 97)
        final += this_char
        print(row_position)

    print(final)




cipher(string)