string = "congratulations you are at least sort of smart"


def reverse_cipher(string):
    final_list = []
    for each in string:
        if each != " ":
            each = chr(123 - (ord(each) - 96))
        final_list.append(each)
    return "".join(final_list)


print(reverse_cipher(string))
