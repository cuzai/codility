import numpy as np
import time
import random
import timeit


def get_test(test_mode):
    if test_mode :
        N = 1000000
        S = [random.choice(["(", ")"]) for _ in range(N)]
    else :
        N = 4
        S = [random.choice(["(", ")"]) for _ in range(N)]
    return "".join(S)

def test(test_mode=False):
    test_li = []
    idx = 0
    time_spent = 0
    for _ in range(100):
        while True:
            S = get_test(test_mode)  ###############
            test = S  ############################
            if test not in test_li:
                test_li.append(test)
                break
            idx += 1

            if idx == 1000:
                print("no more possibility")
                return
        print("got_test")
        start = time.time()
        result = solution(S)  ################
        end = time.time()

        if not test_mode:
            print(f"S : {S} = {result} : {end - start}")  ################
        if test_mode:
            print("\r", _, end="")

        if time_spent < end - start:
            time_spent = end - start
    print()
    print(time_spent)




def solution(S):
    open_bracket = []

    for s in S :
        if s == "(" : open_bracket.append(s)
        else : 
            try :
                del open_bracket[-1]
            except :
                return 0
    if len(open_bracket) == 0 : return 1
    else : return 0



S = "(()(())())"
# print(solution(S))
print(test(test_mode=True))




