def king(N,L):
    moves = [(-1,0),(1,0),(0,1)]
    result = -1
    memo = [[True] * N for _ in range(N)]
    print(memo)
    for w,k in L:
        memo[w][k] = False
    memo[0][0] = False

    def rek(moves,memo,i,j,N,cnt):
        nonlocal result
        if i == N - 1 and j == N - 1:
            result = max(result,cnt)
            return

        flag = False
        for x,y in moves:
            if 0 <= i + x < N and 0 <= j + y < N and memo[i + x][j + y]:
                flag = True
                memo[i + x][j + y] = False
                rek(moves,memo,i + x,j + y,N,cnt + 1)
                memo[i + x][j + y] = True
        if flag:
            return

    rek(moves,memo,0,0,N,0)
    return result if result != -1 else None

N = 4
L = [(0,1),(1,1),(2,1)]
print(king(N,L))



