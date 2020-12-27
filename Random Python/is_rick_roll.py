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


def is_rick_roll(url: str) -> bool:
    """
    Checks if a url matches in the list of known rick-rolls.
    Known Rick Roll for testing: https://seph.club/not-a-rickroll
    :param url: string, the url to be checked
    :return: bool, whether or not this url is suspected to be a rick-roll
    """
    resp = requests.get(url).text
    for roll in known_rolls:
        if roll in resp:
            return True
    return False


if __name__ == "__main__":
    known_rolls = clean_data(raw_rolls)
    test_url = input("paste url here\n")

    print("DANGER! This is a rick-roll" if is_rick_roll(test_url) else "This is not a known rick-roll, "
                                                                       "but be cautious, they are crafty!")
