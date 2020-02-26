import multiprocessing
import time

run_multi = True


def intense_list_gen(seed=3):
    this_list = [x ** seed for x in range(10000000)]
    print(sum(this_list))


if __name__ == '__main__':

    start_time = time.perf_counter()

    if run_multi:
        processes = []

        for _ in range(5):
            p = multiprocessing.Process(target=intense_list_gen)
            p.start()
            processes.append(p)

        for process in processes:
            process.join()
    else:
        for _ in range(5):
            intense_list_gen()

    test_time = round(time.perf_counter() - start_time, 3)
    print(f'Total Time was: {test_time} second(s)')

