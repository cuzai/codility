def solution(A):
    disc = sorted([[n-a, n+a]  for n, a in enumerate(A)])
    # print(disc)
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

    # val_val = 0
    # for i in range(N) :
    #     for j in range(i+1, N) :
    #         if disc[i][1] >= disc[j][0] :
    #             val_val += 1
    # print(val_val)

    return val

"""
주어진 원들이 교차하는 횟수를 구하는 문제
못풀겠음
==> 이진 탐색 활용 풀어야 함
"""
