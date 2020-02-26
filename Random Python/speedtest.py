from time import time
import argparse


def multiply(difficulty: int, iterations=30):
    duration = 10**(difficulty * 128)
    final = []
    initial_time = time()
    for test in range(iterations + 1):
        start_time = time()
        x = 1
        while x < duration:
            print(x)
            x = x * 2
        end_time = time()
        final.append(end_time - start_time)
    print(f'Total Time: {str(time() - initial_time)[0:6]} seconds\nAverage Time Per Test: {str(sum(final)/len(final))[0:6]} seconds')


if __name__ == '__main__':
    multiply(7)
