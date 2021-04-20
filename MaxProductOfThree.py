def solution(A):
    A = sorted(A)
    with_minus = A[0]*A[1]*A[-1]
    only_plus = A[-1]*A[-2]*A[-3]
    return max(with_minus, only_plus)

"""
주어진 배열에서 3 개 곱의 결과가 가장 큰 조합 찾아내는 문제
"""