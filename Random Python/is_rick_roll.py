import requests
from typing import List

with open("rick_rolls.txt", "r") as f:
    raw_rolls = f.read()


def is_link(check_link: str) -> bool:
    return "www." in check_link


def clean_data(inp: str) -> List[str]:
    data = inp.split("\n")
    final_data = []

    for each in data:
        if len(each) > 0:
            if is_link(each):
                if "(" in each:
                    each = each.split("(")[0]
                final_data.append(each)
    return final_data


known_rolls = clean_data(raw_rolls)

# test_rick_roll_url = "https://seph.club/not-a-rickroll" #  this one should currently be a positive

this_url = input("paste url here\n")

resp = requests.get(this_url).text


is_rick_roll = False

for roll in known_rolls:
    if roll in resp:
        is_rick_roll = True


was_roll = "DANGER! This is a rick-roll" if is_rick_roll else "Caution: This is not a known rick-roll"

print(was_roll)
