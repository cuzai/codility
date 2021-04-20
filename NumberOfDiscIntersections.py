def solution(A):
    val = 0
    disc = [[n - a, n + a] for n, a in enumerate(A)]

    for idx_1 in range(len(disc)):
        if val > 10000000:
            return -1
        for idx_2 in range(idx_1 + 1, len(disc)):
            if disc[idx_1][1] >= disc[idx_2][0]:
                val += 1
    return val


A = [1, 5, 2, 1, 4, 0]
print(solution(A))

"""
주어진 원들이 교차하는 횟수를 구하는 문제
못풀겠음
"""
