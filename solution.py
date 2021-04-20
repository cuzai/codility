import numpy as np
import time
import random
import timeit


def get_test(test_mode):
    if test_mode:
        N = random.randint(0, 100000)
        A = [random.randint(0, 2147483647) for _ in range(N)]
    else:
        N = random.randint(0, 10)
        A = [random.randint(0, 10) for _ in range(N)]
    return A


def test(test_mode=False):
    test_li = []
    idx = 0
    time_spent = 0
    for _ in range(100):
        while True:
            A = get_test(test_mode)  ###############
            test = A  ############################
            if test not in test_li:
                test_li.append(test)
                break
            idx += 1

            if idx == 1000:
                print("no more possibility")
                return
        print("got_test")
        start = time.time()
        result = solution(A)  ################
        end = time.time()

        if not test_mode:
            print(f"A : {A} = {result} : {end - start}")  ################
        if test_mode:
            print("\r", _, end="")

        if time_spent < end - start:
            time_spent = end - start
    print()
    print(time_spent)


def solution(A):
    val = 0
    disc_high = [n + a for n, a in enumerate(A)]
    disc_low = [n - a for n, a in enumerate(A)]

    for high_idx in range(len(disc_high)):
        for low_idx in range(high_idx + 1, len(disc_low)):
            if disc_high[high_idx] >= disc_low[low_idx]:
                val += 1
    return val


A = [1, 5, 2, 1, 4, 0]
print(solution(A))
# print(test(test_mode=True))
