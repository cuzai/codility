def solution(N):
    N = bin(N)[2:]
    one_idx = [n for n, i in enumerate(N) if i == "1"]
    gap = 0
    for i in range(len(one_idx) - 1):
        new_gap = one_idx[i + 1] - one_idx[i] - 1
        if new_gap > gap:
            gap = new_gap

    return gap


N = 1041
print(solution(N))

"""
수를 이진수로 만들고
1과 1 사이에 있는 0의 개수를 찾는 문제
"""
