pairs = {
    'a': [1],
    'b': [1, 2],
    'c': [1, 4],
    'd': [1, 4, 5],
    'e': [1, 5],
    'f': [1, 2, 4],
    'g': [1, 2, 4, 5],
    'h': [1, 2, 5],
    'i': [2, 4],
    'j': [2, 4, 5],
    'k': [1, 3],
    'l': [1, 2, 3],
    'm': [1, 3, 4],
    'n': [1, 3, 4, 5],
    'o': [1, 3, 5],
    'p': [1, 2, 3, 4],
    'q': [1, 2, 3, 4, 5],
    'r': [1, 2, 3, 5],
    's': [2, 3, 4],
    't': [2, 3, 4, 5],
    'u': [1, 3, 6],
    'v': [1, 2, 3, 6],
    'w': [2, 4, 5, 6],
    'x': [1, 3, 4, 6],
    'y': [1, 3, 4, 5, 6],
    'z': [1, 3, 5, 6],
    'upper': [6],
    ' ': []
}


def create_binary(letter):
    this_bin = ['0' for x in range(6)]
    for dot in pairs[letter]:
        this_bin[dot - 1] = '1'
    return ''.join(this_bin)


def solution(s):
    final = ''
    for letter in s:
        this_bin = ''
        if letter.upper() == letter and letter != ' ':
            this_bin = create_binary('upper')
        this_bin += create_binary(letter.lower())

        final += this_bin

    return final


def to_braille(binary):
    output = []
    for count, value in enumerate(binary):
        if value == '1':
            output.append(count+1)
    return output


def check_binary(string):
    final_list = []
    binary_list = [string[i:i+6] for i in range(0, len(string), 6)]

    for each in binary_list:
        braille = to_braille(each)
        if braille in pairs.values():
            for key, value in pairs.items():
                if braille == value:
                    final_list.append({key: each})
        else:
            final_list.append({each: "NO MATCH"})

    return final_list


this_solution = solution('The quick brown fox jumps over the lazy dog')

print(check_binary(this_solution))
