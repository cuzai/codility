def solution(A):
    A = sorted([a for a in A if a > 0])

    # validation code
    # for i in range(len(A)-2) :
    #     for j in range(i+1, len(A)-1) :
    #         for z in range(j+1, len(A)) :
    #             if A[i]+A[j] > A[z] :
    #                 return 1
    # return 0

    # real_code
    for i in range(len(A)-2) :
        if A[i] + A[i+1] > A[i+2] :
            return 1
    return 0

    """
    A의 원소 중 3개가 P < Q < R 일 떄
    P+Q > R
    P+R > Q
    Q+R > P
    인 값을 찾는 문제
    증명을 통해 값이 모두 0보다 커야 한다 정도만 알아 냄

    그냥 돌려도 웬만큼 성능은 나오는데
    정답의 규칙(붙어 있는 원소들만 봐도 되는 것)을 알기가 어려움
    """