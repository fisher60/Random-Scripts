import random


def run_match():
    sum = 0

    for _ in range(7):
        print("game")
        if random.randint(0, 100) < 60:
            sum += 1
            if sum == 4:
                print("win")
                break
    else:
        print("LOSE")


for match in range(10**5):
    run_match()
