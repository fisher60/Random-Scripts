conversion_table = {"a": "t", "t": "a", "g": "c", "c": "g"}

def convert():
    test = input("enter DNA string")
    final = ""
    for each in test:
        final += (conversion_table[each])

    final_dna = ""
    for count, item in enumerate(final):
        if item == "a":
            item = "u"
        elif item == "t":
            item = "a"
        final_dna += item

    print(f'RNA: {final}\nDNA: {final_dna}')
    check = input("would you like to do another, y/n?")
    if "y" in check:
        return convert()
    else:
        return 1

convert()
