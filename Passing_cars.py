def solution(A):
    west_cnt = sum(A)
    result = 0
    for a in A:
        if a == 0:
            result += west_cnt
            if result > 1000000000:
                return -1
        else:
            west_cnt -= 1
    return result


A = [0, 1, 0, 1, 1]
print(solution(A))

"""
동쪽으로 가는 차 0
서쪽으로 가는 차 1
차끼리 서로 마주치는 횟수 구하는 문제
"""
