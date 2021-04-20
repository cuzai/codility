def solution(A, K):
    if len(A) == 0:
        return []
    K = K % len(A)
    first = A[len(A) - K :]
    second = A[: len(A) - K]
    return first + second


"""
주어진 배열 A를 K만큼 움직이는 문제
"""
