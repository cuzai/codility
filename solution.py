import numpy as np
import time
import random
import timeit


def get_test(test_mode):
    if test_mode :
        N = random.randint(0, 100000)
        A = [random.randint(0, 2147483647) for _ in range(N)]
    else :
        N = random.randint(0, 5)
        A = [random.randint(0, 5) for _ in range(N)]
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
    disc = sorted([[n-a, n+a]  for n, a in enumerate(A)])
    print(disc)
    N = len(disc)
    val = 0
    for i in range(N-1) :
        if val > 10000000 :
            return -1
        # find x <= target
        target = disc[i][1]
        start = i+1
        end = N-1

        if target < disc[start][0] :
            continue
        elif target >= disc[end][0] :
            val += end-start+1
            continue
        
        while True :
            mid = (start+end)//2
            if target >= disc[mid][0] and target < disc[mid+1][0] :
                val += mid- (i+1) + 1
                break
            if target >= disc[mid][0] :
                start = mid + 1
            elif target < disc[mid][0] : 
                end = mid -1

    val_val = 0
    for i in range(N) :
        for j in range(i+1, N) :
            if disc[i][1] >= disc[j][0] :
                val_val += 1
    print(val_val)

    return val



A = [0, 1, 2, 3, 0]
print(solution(A))
# print(test(test_mode=False))




