def solution(A):
    if len(A) == 1:
        return A[-1]
    A = sorted(A)
    for i in range(0, len(A), 2):
        try:
            if A[i] != A[i + 1]:
                return A[i]
        except IndexError:
            return A[-1]


A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))


"""
개수가 짝수인 수끼리 pair 해 주고 남는 수 찾는 문제
"""
